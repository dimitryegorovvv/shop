from django.shortcuts import render, redirect
from .forms import PaymentForm
from .paypal import paypalrestsdk

def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            paypal_payment = paypalrestsdk.Payment({
                "intent": "sale",
                "payer": {
                    "payment_method": "paypal"},
                "transactions": [{
                    "amount": {
                        "total": str(payment.amount),
                        "currency": payment.currency},
                    "description": payment.description}],
                "redirect_urls": {
                    "return_url": "https://d28f-178-120-67-229.ngrok-free.app/payments/execute/",
                    "cancel_url": "https://d28f-178-120-67-229.ngrok-free.app/payments/cancel/"}})
            
            if paypal_payment.create():
                for link in paypal_payment.links:
                    if link.rel == "approval_url":
                        approval_url = link.href
                        payment.save()
                        return redirect(approval_url)
            else:
                print(paypal_payment.error)
    else:
        form = PaymentForm()

    return render(request, 'create_payment.html', {'form': form})

def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        print("Payment executed successfully")
        return redirect('success')
    else:
        print(payment.error)
        return redirect('failure')
    
def success(request):
    return render(request, 'success.html')

def failure(request):
    return render(request, 'failure.html')

def cancel_payment(request):
    return render(request, 'cancel.html')