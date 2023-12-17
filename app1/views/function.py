import os.path

from django.shortcuts import render

# Create your views here.
# 基础模块
from django.shortcuts import render, HttpResponse
from django.conf import settings

# function模块
from app1.untils import TranPic


def index(request):
    return render(request, "function.html")


def funTranPic(request):
    if request.method == "GET":
        contentPicExa_path = "tmp/function/TranPic/input/content_example.jpg"
        stylePicExa_path = "tmp/function/TranPic/input/style_example.jpg"
        resultExa_path = "tmp/function/TranPic/output/result_example.jpg"
        return render(request, "funTranPic.html",
                      {"contentPic_path": contentPicExa_path, "stylePic_path": stylePicExa_path,
                       "result_path": resultExa_path})

    contentPic_fildObj = request.FILES.get("contentPic")
    contentPic_path = os.path.join("app1","static","tmp", "function", "TranPic", "input", "content.jpg")
    print(contentPic_fildObj)
    f = open(contentPic_path, mode='wb')
    for chunk in contentPic_fildObj.chunks():
        f.write(chunk)
    f.close()

    stylePic_fildObj = request.FILES.get("stylePic")
    stylePic_path = os.path.join("app1","static","tmp", "function", "TranPic", "input", "style.jpg")
    print(stylePic_fildObj)
    f = open(stylePic_path, mode='wb')
    for chunk in stylePic_fildObj.chunks():
        f.write(chunk)
    f.close()

    resultPic_path = os.path.join("app1","static","tmp", "function", "TranPic", "output", "content+style.jpg")

    TP = TranPic.TranPic(contentPic_path, stylePic_path, resultPic_path)

    DcontentPic_path = "tmp/function/TranPic/input/content.jpg"
    DstylePic_path = "tmp/function/TranPic/input/style.jpg"
    DresultPic_path = "tmp/function/TranPic/output/content+style.jpg"

    return render(request,"funTranPic.html",{"contentPic_path": DcontentPic_path, "stylePic_path": DstylePic_path,
                       "result_path": DresultPic_path})
