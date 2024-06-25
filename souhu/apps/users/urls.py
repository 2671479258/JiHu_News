from django.contrib import admin
from django.urls import path, include
from users import views


urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('logout/',views.LogoutView.as_view()),
    path('get_profile/',views.GetProfile.as_view()),
    path('get_userinfo/', views.GetUserInfo.as_view()),
path('upload_avatar/', views.upload_avatar.as_view())
]