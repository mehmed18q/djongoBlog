from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse("Hello Django!\nIm Sadeq Nice to meet you.")
    return render(request, 'about.html')


def home(request):
    # return HttpResponse("Hello Django!\nIt's Your New Home.")
        return render(request, 'home.html')

def NotFound(request):
    # return HttpResponse("Hello Django!\nIt's NotFound 404-Error.")
        return render(request, 'NotFound.html')
