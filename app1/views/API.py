from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "API.html")

def soundCode(request):
    return render(request, "soundCode.html")

def soundCodeTranPic(request):
    return render(request, "soundCodeTranPic.html")
