from django.urls import path
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('payments/', views.payments, name='payments'),
    path('cod_payment/', views.cod_payment, name='cod_payment'),   # NEW: Cash on Delivery
    path('order_complete/', views.order_complete, name='order_complete'),
]