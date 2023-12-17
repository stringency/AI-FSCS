from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "community.html")

def soundCodeCommunity(request):
    return render(request, "soundCodeCommunity.html")

def communityTranPic(request):
    return render(request, "communityTranPic.html")


