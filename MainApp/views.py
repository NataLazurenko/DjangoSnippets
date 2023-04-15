from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.forms import SnippetForm
from MainApp.models import Post
from MainApp.forms import UserRegisterForm
from django.contrib import messages


def Login(request):
    return render(request, 'users/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('home')
    if request.method == "GET":
        form = UserRegisterForm()
        context = {
            'form':form,
            'pagename':'Регистрация',
        }
        return render(request,'users/register.html',context)
def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {'pagename':'Добавение нового сниппета',"form":form}
        return render(request, 'pages/add_snippet',context)
    if request.method == "POST":
       form = SnippetForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("redirect_url")
       return render(request,'add_snippet.html',{'form': form})


def index_page(request):
    context = {'pagename': 'PythonBin',
             'posts': Post.objects.all(),
               }
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    context = {'pagename': 'Просмотр сниппетов'}
    return render(request, 'pages/view_snippets.html', context)
