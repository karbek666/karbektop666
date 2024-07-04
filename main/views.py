from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.views.generic import DetailView
from .forms import LoginForm, RegisterForm, SampleModelForm, MessageForm
from .models import Ween, Profile, Book_list, Corzina, Image_ween, BuyModel
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def index(request):
    dom = Ween.objects.filter(is_purchased=False)
    response = render(request, 'books.html', {'doms': dom})
    return response


@login_required
def profile(request):
    user = request.user
    profile = user.profile
    return render(request, 'profile.html', {'profile': profile})

@login_required
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
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.user = request.user
            purchase.save()
            for image in request.FILES.getlist('images'):
                img_obj = Image_ween.objects.create(img=image)
                purchase.images.add(img_obj)
            return redirect('my_sell')
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

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def poderca(request):
    response = render(request, 'poderca.html', {'podercas': poderca})
    return response

class WeenDetailView(DetailView):
    model = Ween
    template_name = 'detail.html'
    context_object_name = 'ween'

class Buy_views(DetailView):
    model = BuyModel
    template_name = 'buy.html'
    context_object_name = 'buy'
from .forms import BuyForm
@login_required
def process_payment(request, book_id):
    book = get_object_or_404(Book_list, id=book_id)
    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid():
            buy = form.save(commit=False)
            buy.user = request.user
            buy.book = book

            # Расчет суммы на основе цены дома
            buy.amount = book.tour.price
            buy.save()

            # Обновление статуса is_purchased у соответствующего тура
            tour = book.tour
            tour.is_purchased = True
            tour.save()

            # Перенаправление на страницу с информацией о бронировании
            return redirect('book')
    else:
        form = BuyForm()
    return render(request, 'payment.html', {'form': form, 'book': book})
@login_required
def delete_favorite(request, pk):
    if request.method == 'POST':
        type = request.POST.get('type')
        if type == 'book_list':
            favorite_item = get_object_or_404(Book_list, pk=pk)
            favorite_item.delete()
            return redirect('poderka')


@login_required
def my_sell(request):
    my_sells = Ween.objects.filter(user=request.user)
    response = render(request, 'my_sell.html', {'my_sells': my_sells})
    return response

def delete_my_sell(request, pk):
    if request.method == 'POST':
        type = request.POST.get('type')
        if type == 'book_list':
            favorite_item = get_object_or_404(Ween, pk=pk)
            favorite_item.delete()
            return redirect('my_sell')

class My_purchases(DetailView):
    model = Ween
    template_name = 'my_purchases.html'
    context_object_name = 'pk'



# @login_required
# def send_message(request, seller_id):
#     seller = get_object_or_404(User, id=seller_id)
#
#     if request.method == 'POST':
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             message = form.save(commit=False)
#             message.sender = request.user
#             message.recipient = seller
#             message.save()
#
#     else:
#         form = MessageForm()
#
#     return render(request, 'send_message.html', {'form': form, 'seller': seller})
