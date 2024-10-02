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

@login_required
def CreateTweet(request):
    if request.method == 'POST' :
        form = TweetForm(request.POST,request.FILES)
        if form.is_valid() :
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else :
        form = TweetForm()
    return render(request,'tweet_form.html', {'form':form})

@login_required
def EditTweet(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.user == tweet.user :
        if request.method == 'POST' :
            form = TweetForm(request.POST,request.FILES,instance=tweet)
            if form.is_valid() :
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()
                return redirect('tweet_list')
        else :
            form = TweetForm(instance=tweet)
    else :
        return redirect('tweet_list')
    return render(request,'tweet_form.html', {'form':form})

@login_required
def DeleteTweet(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list.html')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})

def register(request):
    if request.method == 'POST' :
        form = UserRegisterForm(request.POST)
        if form.is_valid() :
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user = form.save()
            login(request,user)
            return redirect('tweet_list')
    else :
        form = UserRegisterForm()
    return render(request,'register.html', {'form':form})
