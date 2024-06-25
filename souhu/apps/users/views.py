import json
import re

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from users.models import User


class LoginView(View):
    def post(self,request):
        data = json.loads(request.body)

        username = data.get('username')
        password = data.get('password')


        if not all(['username','password']):
            return JsonResponse({'code':400,'errmsg':'参数不全'})

        if re.match(r'1[3-9]\d{9}',username):
            User.USERNAME_FIELD='mobile'
        else:
            User.USERNAME_FIELD='username'

        user=authenticate(username=username,password=password)
        if user is None:
            return JsonResponse({'code':400,'errmsg':'账号或密码错误'})


        login(request,user)
        response=JsonResponse({'code':0,'errmsg':'ok'})
        response.set_cookie('username',username,max_age=3600*24*15)

        return response

class LogoutView(View):
    def delete(self,request):
        logout(request)

        response=JsonResponse({'code':400,'errmsg':'ok'})
        response.delete_cookie('username')

        return response

class GetProfile(View):
    def get(self, request):
        username = request.COOKIES.get('username')
        print(username)
        user = User.objects.filter(mobile=username).first()

        profile = None
        if user is not None:
            profile = user.profile
        print(profile)

        return JsonResponse({'profile': profile})


class GetUserInfo(View):
    def get(self,request):
        mobile = request.COOKIES.get('username')

        user = User.objects.filter(mobile=mobile).first()
        profile = user.profile
        area=user.area
        username=user.username
        userinfo={
            "mobile":mobile,
            "profile":profile,
            "username":username,
            'area':area
        }

        return JsonResponse({'userinfo':userinfo})


class upload_avatar(View):
    def post(self,request):
        try:

            if request.method == 'POST' and request.FILES['avatar']:
                avatar = request.FILES['avatar']
                mobile = request.COOKIES.get('username')
                user = User.objects.filter(mobile=mobile).first()
                user_id = user.id

                with open(f'D:/python/bishe/搜狐新闻/front/images/profile/{user_id}.png', 'wb+') as destination:
                    for chunk in avatar.chunks():
                        destination.write(chunk)
                return JsonResponse({'message': 'Avatar uploaded successfully'}, status=200)
            else:
                return JsonResponse({'error': 'No file found'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)