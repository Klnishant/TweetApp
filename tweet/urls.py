from django.urls import path

from . import views

urlpatterns = [
    path('',views.tweet_list,name='tweet_list'),
    path('create/',views.CreateTweet,name='tweet_create'),
    path('<int:tweet_id>/edit/',views.EditTweet,name='tweet_edit'),
    path('<int:tweet_id>/delete/',views.DeleteTweet,name='tweet_delete'),
    path('register/',views.register,name='register')
]