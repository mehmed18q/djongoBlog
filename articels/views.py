from django.shortcuts import render, HttpResponse, redirect
from . import models # import models
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
# request paramter for django and most be here

def articelsList(request):
    articels = models.Articel.objects.all().order_by('-date') # get all models and sort by date
    args = {"articels" : articels} # Se t Model in args to send to view
    return render(request, GetViewName('articelsList'), args)

def articelDetial(request, slug):
    # return HttpResponse(slug)
    articel = models.Articel.objects.get(slog = slug)
    args = {"articel" : articel} # Set Model in args to send to view
    return render(request, GetViewName('articelDetial'), args)


@login_required(login_url = "/accounts/Login")
def CreateArticle(request):
    if (request.method == 'POST'):
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid:
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('articel:List')
    else:
        form = forms.CreateArticle()
        return render(request, GetViewName('CreateArticle'), {"form": form})

# Return Name of View 
def GetViewName(functionName:str)->str:
    return f"articels/{functionName}.html"