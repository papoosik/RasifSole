from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django import forms
from .forms import *


def index_view(request):
    categories = Category.objects.all()
    return render(request, template_name='app/index.html', context={'categories': categories})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Создает пользователя и сохраняет его в базе данных
            login(request, user)  # Авторизует пользователя после регистрации
            return redirect('index')  # Перенаправляет на главную страницу после регистрации
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


def add_to_cart(request, product_id):
    product = get_object_or_404(Shoes, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_view')


def cart_view(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart/cart_view.html', {'cart_items': cart_items})


def detail_view(request, pk):
    shoe = Shoes.objects.get(id=pk)
    shoes_id = pk
    categories = Category.objects.all()
    return render(request, template_name='app/detail.html', context={'shoe':shoe, 'categories':categories, 'shoes_id': shoes_id})

def catalog_view(request, title_of_category):
    category = Category.objects.get(title=title_of_category)
    shoes_by_category = Shoes.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, template_name='app/catalog.html', context={'shoes_by_category': shoes_by_category, 'categories':categories, 'category': category})


def create_shoes(request):
    if request.method == 'POST':
        form = ShoesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the 'index' view after successful submission
    else:
        form = ShoesForm()

    return render(request, 'app/create_product.html', {'form': form})


def update_shoes(request, shoes_id):
    shoes = get_object_or_404(Shoes, id=shoes_id)

    if request.method == 'POST':
        form = ShoesForm(request.POST, request.FILES, instance=shoes)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ShoesForm(instance=shoes)

    return render(request, 'app/update_product.html', {'form': form})


def delete_shoes(request, shoes_pk):
    shoes = get_object_or_404(Shoes, id=shoes_pk)

    if request.method == 'POST':
        shoes.delete()
        return redirect('index')

    return render(request, 'app/delete_shoes.html', {'shoes': shoes})
