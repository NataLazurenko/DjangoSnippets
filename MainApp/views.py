from django.http import Http404
from django.shortcuts import render, redirect
from .models import Post, Profile
from .forms import UserRegisterForm, SnippetForm, UserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login, logout
from Snippets import settings

@login_required
def profile(request):
    if request.method == "GET":
        print(profile.image)
        form = UserProfile()
        context = {
            'form': form,
            'pagename': 'Профиль',
            "profile": profile
        }
    else:
        form = UserProfile(request.POST, request.FILES)
        if form.is_valid():
            temp_form = form.save(commit=False)
            temp_form.user = request.user
            temp_form.image = form.cleaned_data.get('image')
            temp_form.save()
            messages.success(request, "Вы успешно изменили свой профиль")
        else:
            messages.warning(request,"Ошибка!")
        context = {
            'form': form,
            'pagename': 'Профиль',
        }
    return render(request, 'users/profile.html', context)


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
                return redirect(settings.LOGIN_REDIRECT_URL)
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
def logout_request(request):
    logout(request)
    return render(request, 'users/logout.html')
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
