from django.http import Http404
from django.shortcuts import render, redirect
from .forms import SnippetForm
from .models import Post
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login

def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, "Вы успешно зашли.")
            else:
                messages.warning(request,"Пользователь не найден!")
        else:
            messages.warning(request,"Пользователь не найден!")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', context={"form": form})

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
    @login_required
    def profile(request):
        return render(request,'users/profile.html')
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
