from django.contrib import admin
from django.urls import path, include
from news import views
urlpatterns = [
    path('get_news/',views.get_news.as_view()),
    path('get_comments/<int:new_id>/', views.GetComment.as_view(), name='get_comments'),
    path('publish_comments/', views.PublishComment.as_view(), name='punish_comments'),
path('search/', views.SearchView.as_view()),
    path('publish_reply/',views.PublishReply.as_view()),


]
