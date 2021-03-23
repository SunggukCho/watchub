from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm


from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


from django.views.decorators.http import require_POST, require_http_methods
from django.http import JsonResponse

from rest_framework import status
from .models import User

# Create your views here.
@api_view(['POST'])
def signup(request):
    # Client에서 보내온 정보 받기
    # key값이 password를 get 한다.
    password = request.data.get('password')
    passwordConfirmation = request.data.get('passwordConfirmation')

    # 비밀번호 일치 여부 확인
    if password != passwordConfirmation:
        return Response({ 'error': '비밀번호가 일치하지 않습니다.' }, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=request.data.get('username')).count() > 0:
        return Response({'error': '이미 존재하는 아이디입니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # 사용자가 보낸 데이터로 UserSerializer를 통해 데이터 생성
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        # 그냥 저장하고 끝내면 비밀번호 유출 (DB에 그대로 저장)
        user = serializer.save()

        # 비밀번호 해싱
        user.set_password(request.data.get('password'))
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=request.data.get('username')).count() < 1:
        return Response({'error': '아이디를 확인해주세요.'}, status = status.HTTP_400_BAD_REQUEST)
        
    user = get_object_or_404(get_user_model(), username=username)

    if user.check_password(password):
        return Response({'userId': user.id, 'username': user.username}, status= status.HTTP_200_OK)
    else:
        return Response({'error': "비밀번호를 확인해주세요."}, status= status.HTTP_400_BAD_REQUEST)





