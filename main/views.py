from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView

from .forms import LoginForm, RegisterForm, SampleModelForm
from .models import Ween, Profile, Book_list, Corzina, Image_ween


def index(request):
    dom = Ween.objects.all()
    response = render(request, 'books.html', {'doms': dom})
    return response


@login_required
def profile(request):
    user = request.user
    profile = user.profile
    return render(request, 'profile.html', {'profile': profile})


def poderka(request):
    poderka = Book_list.objects.filter(user=request.user)
    response = render(request, 'poderka.html', {'poderka': poderka})
    return response


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('book/')
            else:
                messages.error(request, 'Неверное имя пользователя или пароль. Пожалуйста, попробуйте снова.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def sell(request):
    if request.method == 'POST':
        form = SampleModelForm(request.POST, request.FILES)
        images = request.FILES.getlist('images')
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.user = request.user
            purchase.save()
            for image in images:
                img_obj = Image_ween(img=image)
                img_obj.save()
                purchase.images.add(img_obj)

            return redirect('book')
    else:
        form = SampleModelForm()
    return render(request, 'sell.html', {'form': form})


@login_required
def book_tour(request, pk):
    try:
        tour = Ween.objects.get(pk=pk)
    except Ween.DoesNotExist:
        return HttpResponse("Дом с таким id не найден.", status=404)

    if request.method == 'POST':
        if not Book_list.objects.filter(user=request.user, tour=tour).exists():
            if tour.available_seats > 0:
                Book_list.objects.create(user=request.user, tour=tour)
                tour.available_seats -= 1
                tour.save()
            else:
                messages.error(request, "Извините, все места уже куплены.")
    return redirect('poderka')


def logout_view(request):
    logout(request)
    return redirect('/')


def poderca(request):
    response = render(request, 'poderca.html', {'podercas': poderca})
    return response

def MyDetailView(request, pk):
    model = get_object_or_404(Ween, pk=pk)
    image = Image_ween.objects.filter(ween=model)
    return render(request,"detail.html", {'model': model, 'image': image})



