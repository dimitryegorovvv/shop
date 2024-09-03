from django.urls import path, include
from .views import *

urlpatterns =[
    # path('', include('social_django.urls')),
    path('accounts/reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/register/', CustomRegisterView.as_view(), name='register'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/', include('registration.backends.default.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', redirect_profile),
    path('suggest/token', yandex_auth, name='yandex_auth')
]