from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_lists, name='movie_lists'),    # 영화들
    path('<int:pk>/', views.movie_detail, name='movie_detail'),    # 영화 상세 페이지 & 커뮤니티 리뷰들 보여줌
    path('latest/', views.latest),    # 최신 영화들
    path('classic/', views.classic),    # 옛날 영화들
    path('popular/', views.popular),    # 인기작
    path('genre/', views.genre_lists),   # 장르들
    

    path('<int:movie_id>/reviews/', views.review),   # 리뷰(평점) 작성(POST) 및 리뷰 전체 조회(GET) 
    path('<int:movie_id>/reviews/<int:review_id>/delete/', views.review_delete),    # 리뷰 삭제(DELETE)
    path('<int:movie_id>/reviews/<int:review_id>/update/', views.review_update),    # 리뷰 상세 조회(GET) 및 수정(PUT)


    path('<int:movie_id>/comments/', views.comment),    # 댓글 작성(POST) 및 댓글 전체 조회(GET)
    path('<int:movie_id>/comments/<int:comment_id>/delete/', views.comment_delete),    # 댓글 삭제(DELETE)
    path('<int:movie_id>/comments/<int:comment_id>/update/', views.comment_update),    # 댓글 상세 조회(GET) 및 수정(PUT)

    
    path('<int:pk>/like/', views.like, name='movie_like'),    # 좋아요

    path('<int:pk>/watched/', views.watched,),  # 이미 본 영화 등록(POST)


    path('wish/', views.wish_movie),    # 보고싶은 영화 등록(POST) 보고싶은 영화 조회(GET)
    path('wish/<int:wish_id>/delete/', views.wish_delete),    # 보고싶은 영화 삭제(DELETE)
    path('wish/<int:wish_id>/update/', views.wish_update),    # 보고싶은 영화 상세 조회(GET) 및 수정(PUT)

    
    # 추천 알고리즘
    # 좋아요와 이미 본 영화로 추천하는 것
    path('<int:user_id>/recommend/', views.recommend),
]