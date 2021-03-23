from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Genre, Review, Comment, Wish
from .serializers import RecommendSerializer, ReviewSerializer, ReviewCreateSerializer, GenreSerializer, MovieSerializer, CommentSerializer, CommentCreateSerializer, WishSerializer, MovieLikeSerializer, WishCreateSerializer, MovieWatchSerializer
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated


from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required

from django.db.models import Avg, Q, Count, Sum
import random, operator

from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



# Create your views here.

'''
영화 리스트 Vue
'''
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_lists(request):
    if request.method == 'GET':
        movies = Movie.objects.all()    # 영화들
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    else:
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
최신 영화 100선
'''
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def latest(request):
    movies = Movie.objects.order_by('-release_date')[:100] # 최신 영화 100선
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


'''
옛날 영화 100선
'''
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def classic(request):
    movies = Movie.objects.order_by('release_date')[:100] # 옛날 영화 100선
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


'''
인기 영화 100선
'''
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def popular(request):
    movies = Movie.objects.order_by('-vote_average')[:100] # 인기 영화 100선
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


'''
영화 상세 Vue
'''
@api_view(['PUT', 'DELETE', 'GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_detail(request, pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    if request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
장르 리스트 Vue
'''
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def genre_lists(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializers = GenreSerializer(genres, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    else:
        serializers = GenreSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
영화 평점 등록 Vue
'''
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        serializer = ReviewCreateSerializer(data=request.data)
        try:
            review = Review.objects.filter(movie_id=movie_id).filter(user=request.user)
            review.update(rank=request.data['rank'])
            return Response({
                'rank': request.data['rank']
            })
        except ObjectDoesNotExist:
            if serializer.is_valid(raise_exception=True):
                serializer.save(movie_id=movie_id, user=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        movie = get_object_or_404(Movie, pk=movie_id)
        review, created = Review.objects.get_or_create(movie_id=movie_id, user=request.user)
        if created:
            review.rank = 0
        serializer = ReviewCreateSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)




'''
영화 리뷰 삭제 Vue
'''
@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_delete(request, movie_id, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.user == review.user:
        review.delete()
        return Response({'message': '리뷰 삭제 완료'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'message': '다른 사람의 리뷰는 삭제할 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)


'''
영화 리뷰 수정 Vue
'''
@api_view(['PUT', 'GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update(request, movie_id, review_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'PUT':
        serializer = ReviewSerializer(data=request.data, instance=review)
        if serializer.is_valid(raise_exception=True):
            if request.user == review.user:
                serializer.save()
            else:
                return Response({'message': '다른 사람의 평점은 수정할 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        review = get_object_or_404(Review, pk=review_id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)


'''
댓글 작성 Vue
'''
@api_view(['POST', 'GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_id)
        comments = Comment.objects.filter(movie_id=movie_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    else:
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie_id=movie_id, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
댓글 삭제 Vue
'''
@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_delete(request, movie_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.user:
        comment.delete()
        return Response({'message': '댓글 삭제 완료'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'message': '다른 사람의 글은 삭제할 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)


'''
댓글 수정 Vue
'''
@api_view(['PUT', 'GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_update(request, movie_id, comment_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            if request.user == comment.user:
                serializer.save()
                # return Response({'message': '댓글 수정 완료'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': '다른 사람의 댓글은 수정할 수 없습니다.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        comment = get_object_or_404(Comment, pk=comment_id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)


'''
좋아요 Vue
'''

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    
    if request.method == 'POST':
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)

        serializer = MovieLikeSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = MovieLikeSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)


'''
보고싶은 영화 등록 Vue
'''
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def wish_movie(request):
    if request.method == 'POST':
        serializer = WishCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        wishes = Wish.objects.all()
        serializer = WishSerializer(wishes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


'''
보고싶은 영화 삭제 Vue
'''
@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def wish_delete(request, wish_id):
    wish = get_object_or_404(Wish, pk=wish_id)
    if request.user == wish.user:
        wish.delete()
        return Response({'message': '보고 싶은 영화에서 삭제했습니다.'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'message': '다른 사람의 wish는 삭제할 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)


'''
보고싶은 영화 수정 Vue
'''
@api_view(['PUT', 'GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def wish_update(request, wish_id):
    wish = get_object_or_404(Wish, pk=wish_id)
    if request.method == 'PUT':
        serializer = WishSerializer(data=request.data, instance=wish)
        if serializer.is_valid(raise_exception=True):
            if request.user == wish.user:
                serializer.save()
                # return Response({'message': '보고싶은 영화 수정'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': '다른 사람의 wish는 수정할 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        wish = get_object_or_404(Wish, pk=wish_id)
        serializer = WishSerializer(wish)
        return Response(serializer.data, status=status.HTTP_200_OK)


'''
이미 본 영화 Vue
'''
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def watched(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        if movie.watch_users.filter(pk=request.user.pk).exists():
            movie.watch_users.remove(request.user)
        else:
            movie.watch_users.add(request.user)
        serializer = MovieWatchSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = MovieWatchSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)


'''
추천 알고리즘
'''
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommend(request, user_id):
    if request.method == 'GET':        
        # 유저 1이 안 본 영화들의 데이터 뽑아보기
        # movies = list(Movie.objects.exclude(watch_users = user_id))
        
        # 유저 1이 좋아하는 영화들의 데이터 뽑아보기
        movies = list(Movie.objects.exclude(watch_users = user_id).filter(like_users = user_id))
    
        # 좋아요 한 영화가 이미 본 영화이고, 그 외에 좋아요 누른게 없다면
        if len(movies) == 0:
            # 인기 영화 50가지를 보여준다.
            movies = Movie.objects.order_by('-vote_average')[:50]
            serializer = RecommendSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)    
        
        else:
            # # 유저 1이 좋아하는 영화들의 genre_id 값들 뽑아보기
            user_pick = []
            
            for i in range(len(movies)):
                genre_like = movies[i].genre_ids.all().values('id')
                for j in genre_like:
                    user_pick.append(j.get('id'))

            # 최상위 데이터 4개 뽑기
            count = {}
            for i in user_pick:
                try: count[i] += 1
                except: count[i] = 1

            # 만약 좋아요의 데이터가 부족하다면 인기 영화 50작을 소개해준다.
            if len(count) < 4:
                movies = movies = Movie.objects.order_by('-vote_average')[:50]
                serializer = RecommendSerializer(movies, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

            else:
                scount = sorted(count.items(), key=lambda x: x[1], reverse=True)

                love = scount[0][0]
                like = scount[1][0]
                good = scount[2][0]
                soso = scount[3][0]

                # # 유저 1의 취향을 고려한 영화 (1픽 반드시 포함)
                movies = set(Movie.objects.exclude(watch_users = user_id).filter(genre_ids=love).filter(Q(genre_ids=like) | (Q(genre_ids=good) | Q(genre_ids=soso))))
                serializer = RecommendSerializer(movies, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
