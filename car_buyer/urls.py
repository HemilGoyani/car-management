from django.urls import path, include
from . import views
from online_car_sell_buy.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="car-search"),
    path('car_search_result/', views.serachbox, name= 'car-search-result'),
    path('car-buyer-form/', views.car_buyer, name='car-buyer-form') 
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)