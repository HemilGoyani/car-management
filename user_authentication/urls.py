from django.urls import path, include
from user_authentication. views import index, register_request
from car_seller.views import home
from online_car_sell_buy.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', index, name='index'),
    path("register/", register_request, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', home, name='home'),
    path('car-seller/', include('car_seller.urls')),
    path('car-buyer/', include('car_buyer.urls')),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
