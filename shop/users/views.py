from django.contrib.auth.views import PasswordResetConfirmView, LoginView
from django.views import View
from django.contrib.auth import login
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render, get_object_or_404
from .forms import CustomUserCreationForm
from add_goods.models import CartItem, Goods
from django.contrib.auth.forms import AuthenticationForm
from django.utils.functional import lazy
from add_goods.views import get_quantity_sum
import requests
from django.http import HttpResponseRedirect
from .models import CustomUser, YandexUser


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quantity_sum'] = get_quantity_sum(self.request)
        context['next'] = self.request.GET.get('next', '')
        return context  

    def get_success_url(self):
        next_url = self.request.POST.get('next', self.request.GET.get('next', None))
        print(next_url)
        if next_url and next_url != reverse_lazy('register'):
            return next_url
        return reverse_lazy('home')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.transfer_cart_to_user(self.request, self.request.user)
        return response

    def transfer_cart_to_user(self, request, user):
        cart = request.session.get('cart', {})
        for product_id, quantity in cart.items():
            good = get_object_or_404(Goods, id=product_id)
            try:
                same_good_in_cart = CartItem.objects.get(user=user, good=good)
            except:
                same_good_in_cart = False
            if same_good_in_cart:
                same_good_in_cart.delete()                
            CartItem.objects.create(user=user, good=good, quantity=quantity)
        request.session['cart'] = {}


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('password_reset_complete')  

    def form_valid(self, form):
        user = form.save() 
        login(self.request, user) 
        return redirect(self.success_url)


def redirect_profile(request):
    return reverse_lazy('home')


reverse_lazy_str = lazy(reverse_lazy, str)

class CustomRegisterView(View):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'

    def get(self, request):
        form = self.form_class()
        next_url = request.GET.get('next', reverse_lazy_str('home'))
        return render(request, self.template_name, {'form': form,
                                                     'next': next_url,
                                                     'quantity_sum': get_quantity_sum(request)})

    def post(self, request):
        form = self.form_class(request.POST)
        next_url = request.POST.get('next', reverse_lazy_str('home'))
        if form.is_valid():
            user = form.save()
            login(request, user)
            if next_url == '/accounts/login/':
                return redirect(reverse_lazy('home'))
            else:
                return redirect(next_url)
        return render(request, self.template_name, {'form': form, 'next': next_url})
    

def yandex_auth(request):
    code = request.GET.get('code')
    url = "https://oauth.yandex.ru/token"
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": "5f7d4dec0c084cb380daadfdf7e2771e",
        "client_secret": "9d2b3025b19540a89940aa1c5ef9792e",
        "redirect_uri": "https://d28f-178-120-67-229.ngrok-free.app/suggest/token"
    }
    response = requests.post(url, data=data)
    token_info = response.json()
    access_token = token_info.get('access_token')
    headers = {
        "Authorization": f"OAuth {access_token}"
    }
    response = requests.get("https://login.yandex.ru/info", headers=headers)
    user_info = response.json()
    if user_info:
        user, created = CustomUser.objects.get_or_create(username= ('~yandex_user_' + user_info['id']))
        if created:
            YandexUser.objects.create(
                user=user,
                yandex_id=user_info['client_id'],
                name=user_info.get('real_name', 'no_name')
            )
        login(request, user)
        return redirect(reverse('home'))
    return render(request, 'registration/yandex_auth.html')