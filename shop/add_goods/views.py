from django.shortcuts import render, redirect, get_object_or_404
from .models import Goods, Category, CartItem
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def home(request):
    order = request.GET.get('order', '-popularity')
    goods = Goods.objects.order_by(order)
    for good in goods:
        good.id = str(good.id)

    paginator = Paginator(goods, 18) 
    page_number = request.GET.get('page')
    try:
        page_goods = paginator.page(page_number) 
    except PageNotAnInteger:
        page_goods = paginator.page(1)
    except EmptyPage:
        page_goods = paginator.page(paginator.num_pages) 

    return render(request, 'home.html', {'goods': page_goods,
                                         'cart': get_cart(request),
                                           'quantity_sum': get_quantity_sum(request)})


def good(request, id_of_good):
    good = get_object_or_404(Goods, id=id_of_good)
    good.id = str(good.id)
    good.popularity += 1
    good.save()
    return render(request, 'good.html', {'good': good,
                                         'cart': get_cart(request),
                                         'quantity_sum': get_quantity_sum(request)})


def category(request, name_of_category):
    if name_of_category == 'laptops':
        name_of_category_rus = 'Ноутбуки'
    elif name_of_category == 'smart-watches':
        name_of_category_rus = 'Смарт-часы'
    elif name_of_category == 'TV':
        name_of_category_rus = 'Телевизоры'
    category = get_object_or_404(Category, category=name_of_category_rus)
    order = request.GET.get('order', '-popularity')
    goods = Goods.objects.filter(category=category).order_by(order)
    for good in goods:
        good.id = str(good.id)

    paginator = Paginator(goods, 18) 
    page_number = request.GET.get('page') 
    try:
        page_goods = paginator.page(page_number)  
    except PageNotAnInteger:
        page_goods = paginator.page(1)  
    except EmptyPage:
        page_goods = paginator.page(paginator.num_pages)
    
    return render(request, 'home.html', {'goods': page_goods,
                                         'cart': get_cart(request),
                                           'quantity_sum': get_quantity_sum(request),
                                           'name_of_category_rus': name_of_category_rus})


@require_POST
def add_to_cart(request, id_of_good):
    id_of_good = str(id_of_good)
    cart = get_cart(request)
    if id_of_good not in cart:
        if request.user.is_authenticated:
            good = get_object_or_404(Goods, id=id_of_good)
            CartItem.objects.create(user=request.user, good=good)
        else:
            cart[id_of_good] = 1
            request.session['cart'] = cart
        is_alredy_in_cart = 'Уже в корзине'
    else:
        if request.user.is_authenticated:
            cart_item = get_object_or_404(CartItem, user=request.user, good_id=id_of_good)
            cart_item.delete()
        else:
            del cart[id_of_good]
            request.session['cart'] = cart
        is_alredy_in_cart = 'В корзину'
    return JsonResponse({'quantity_sum': get_quantity_sum(request),
                         'is_alredy_in_cart': is_alredy_in_cart,
                         'result_price': result_price(request)})


def cart(request):
    goods = Goods.objects.all()
    for good in goods:
        good.id = str(good.id)
    return render(request, 'cart.html', {'quantity_sum': get_quantity_sum(request),
                                                'goods': goods,
                                                'cart': get_cart(request),
                                                'result_price': result_price(request)})


@require_POST
def cart_change_quality(request, id_of_good, quantity_of_good):
    good = get_object_or_404(Goods, id=id_of_good)
    if request.user.is_authenticated:
        item = CartItem.objects.get(user=request.user, good_id=id_of_good)
        print(item)
        item.quantity = quantity_of_good
        item.save()
    else:
        cart = request.session.get('cart', {})
        good.id = str(good.id)
        for item in cart:
            if item == good.id:
                cart[item] = quantity_of_good
                break
        request.session['cart'] = cart
    new_price = good.price * quantity_of_good
    return JsonResponse({'quantity_sum': get_quantity_sum(request),
                                'new_price': new_price,
                                'result_price': result_price(request)})


def result_price(request):
    cart = get_cart(request)
    goods = Goods.objects.all()
    result_price = 0
    for good in goods:
        good.id = str(good.id)
        for good_id_cart, value in cart.items():
            if good_id_cart == good.id:
                result_price += value * good.price 
    result_price = "{:.2f}".format(round(result_price, 2)).rstrip('0').rstrip('.').replace(".", ",")
    return result_price


def get_quantity_sum(request):
    cart = get_cart(request)
    quantity_sum = 0
    for cart_quantity in cart.values():
        quantity_sum += cart_quantity
    return quantity_sum


def get_cart(request):
    if request.user.is_authenticated:
        user_cart = CartItem.objects.filter(user=request.user)
        cart = {}
        for cart_item in user_cart:
            cart[str(cart_item.good.id)] = cart_item.quantity
    else:
        cart = request.session.get('cart', {})
    return cart