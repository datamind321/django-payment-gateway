from django.urls import path 
from .views import create_payment,payment_success,payment_failed

urlpatterns = [
    path('create-payment/',create_payment,name='create_payment'),
    path('payment-success/',payment_success,name='payment_success'),
    path('payment-failed/',payment_failed,name='payment_failed'),
]