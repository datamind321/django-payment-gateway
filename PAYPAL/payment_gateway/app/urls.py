from django.urls import path
from .views import payment_checkout,create_payment,execute_payment,payment_failed
urlpatterns = [
    path('checkout/',payment_checkout,name='checkout_payment'),
    path('create_payment/',create_payment,name='create_payment'),
    path('payment_failed/',payment_failed,name='payment_failed'),
    path('execute_payment/',execute_payment,name='execute_payment'),
]