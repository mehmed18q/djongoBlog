from django.shortcuts import render, HttpResponse
from . import models # import models

# Create your views here.
# request paramter for django and most be here

def articelsList(request):
    articels = models.Articel.objects.all().order_by('-date') # get all models and sort by date
    args = {"articels" : articels} # Set Model in args to send to view
    return render(request, GetViewName('articelsList'), args)

def articelDetial(request, slug):
    # return HttpResponse(slug)
    articel = models.Articel.objects.get(slog = slug)
    args = {"articel" : articel} # Set Model in args to send to view
    return render(request, GetViewName('articelDetial'), args)

# Return Name of View 
def GetViewName(functionName:str)->str:
    return f"articels/{functionName}.html"