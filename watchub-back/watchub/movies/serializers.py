from rest_framework import serializers
from .models import Movie, Genre, Review, Comment, Wish

# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(many=True, read_only=True)

    
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'vote_average', 'release_date', 'overview', 'genre_ids',)


class MovieLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'like_users',)


class MovieWatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'watch_users',)


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'rank', 'created_at', 'updated_at', 'movie_id', 'user_id',)


class ReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('rank',)
        

class CommentSerializer(serializers.ModelSerializer):

    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'updated_at', 'movie_id', 'user_id', 'user', )


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('content',)


class WishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wish
        fields = ('id', 'title', 'user_id',)


class WishCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wish
        fields = ('title',)


class RecommendSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(many=True, read_only=True)
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'vote_average', 'release_date', 'overview', 'genre_ids', 'like_users', 'watch_users', 'user',)

