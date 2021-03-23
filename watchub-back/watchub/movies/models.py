from django.db import models
from django.conf import settings


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)  # 장르

class Movie(models.Model):
    genre_ids = models.ManyToManyField(Genre)   # 영화 장르
    title = models.CharField(max_length=100)   # 영화 제목
    poster_path = models.CharField(max_length=200) # 영화 썸네일
    vote_average = models.FloatField() # 영화 평점
    release_date = models.DateField()   # 영화 개봉일
    overview = models.TextField()   # 영화 줄거리
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    watch_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='watch_movies')


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   # 리뷰 작성자
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  #하나의 영화에 여러개의 평점 작성
    rank = models.IntegerField(blank=True, null=True)  # 영화 평점
    created_at = models.DateTimeField(auto_now_add=True)    # 생성시각
    updated_at = models.DateTimeField(auto_now=True)    # 수정시각


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)    # 댓글 작성자
    content = models.CharField(max_length=100)  #   영화에 대한 comment
    created_at = models.DateTimeField(auto_now_add=True)    # 생성시각
    updated_at = models.DateTimeField(auto_now=True)    # 수정시각


class Wish(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)   # 보고싶은 영화 제목
