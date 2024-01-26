from django.shortcuts import render,redirect
import paypalrestsdk
from django.conf import settings
from django.urls import reverse

paypalrestsdk.configure(
    {
        'mode':'sandbox',   # change to live for production
        'client_id':settings.PAYPAL_CLIENT_ID,
        'client_secret':settings.PAYPAL_SECRET,
    })

print('all fine')

def create_payment(request):
    payment = paypalrestsdk.Payment({
        'intent':'sale',
        'payer':{
            'payment_method':'paypal',
        },
        'redirect_urls':{
         'return_url':request.build_absolute_uri(reverse('execute_payment')),
        'cancel_url':request.build_absolute_uri(reverse('payment_failed')),
        },
        'transactions':[
            {
                'amount':{
                    'total':'10.00',
                    'currency':'USD',
                },
                'description':'Payment for Product/Service',
            }
        ],
    })

    if payment.create():
        return redirect(payment.links[1].href)
    else:
        return render(request,'app/payment_failed.html')


def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({'payer_id':payer_id}):
        return render(request,'app/payment_success.html')
    else:
        return render(request,'app/payment_failed.html')
    

def payment_checkout(request):
    return render(request,'app/checkout.html')

def payment_failed(request):
    return render(request, 'app/payment_failed.html')





# Create your views here.




# 