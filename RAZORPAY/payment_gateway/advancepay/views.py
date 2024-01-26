from django.shortcuts import render
import razorpay   
from django.conf import settings



def create_payment(request):
    if request.method=='POST':
        amount = int(request.POST['amount']) * 100   # amount in paise
        client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY,settings.RAZORPAY_API_SECRET))
        print(client)
        payment_data = {
            'amount':amount,
            'currency':'INR',
            'receipt':'order_receipt',
            'notes':{
                'email':'user_email@example.com',
            },
        }

        order = client.order.create(data=payment_data)
        print(order)
        order_id = order['id'] 
        response_data = {
            
            "id":order["id"],
            "amount":order["amount"],
            "currency":order["currency"],
            "key":settings.RAZORPAY_API_KEY,
            "name":"ShoppinglyX",
            "description": "Payment For Your Product",
            "image":"https://previews.123rf.com/images/ikalvi/ikalvi1712/ikalvi171200242/92412982-smiling-shopping-cart-vector-logo-design-shopping-mart-or-app-vector-logo.jpg"
        }

        return render(request,'advancepay/payment.html',response_data)
    return render(request,'advancepay/payment.html')


def payment_success(request):
    return render(request,'advancepay/payment_success.html')



def payment_failed(request):
    return render(request,'advancepay/payment_failed.html')

