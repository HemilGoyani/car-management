from django.urls import path, include
from . import views
from online_car_sell_buy.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="car-search"),
    path('car-search-result/', views.serachbox, name= 'car-search-result'),
    path('car-search-result/car-buyer-form/<int:id>', views.car_buyer, name='car-buyer-form'),
    path('car-buyer-save/<int:id>', views.car_buyer_save, name='car-buyer-save')
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)