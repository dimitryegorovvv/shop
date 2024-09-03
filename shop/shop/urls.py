from django.contrib import admin
from django.urls import path, include
from add_goods import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('auth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:id_of_good>/', views.add_to_cart, name='add_to_cart'),
    path('cart/cart_change_quality/<int:id_of_good>/<int:quantity_of_good>/', views.cart_change_quality, name='cart_change_quality'),
    path('', include('users.urls')),
    path('payments/', include('payments.urls')),
    path('good/<int:id_of_good>/', views.good, name='good'),
    path('category/<str:name_of_category>/', views.category, name='category'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
