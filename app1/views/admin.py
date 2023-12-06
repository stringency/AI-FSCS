from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse

def admin_register(request):
    return render(request, "admin_register.html")

def admin_index(request):
    return render(request, "admin_index.html")

def admin_indexfront(request):
    return render(request, "admin_indexfront.html")


