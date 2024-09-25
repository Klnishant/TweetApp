from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegisterForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})
