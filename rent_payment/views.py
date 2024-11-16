# rent_payment/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Payment
from .forms import PaymentForm

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'rent_payment/payment_list.html', {'payments': payments})

def payment_create(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'rent_payment/payment_form.html', {'form': form})

def payment_update(request, paymentId):
    payment = get_object_or_404(Payment, paymentId=paymentId)
    if request.method == "POST":
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'rent_payment/payment_form.html', {'form': form})

def payment_delete(request, paymentId):
    payment = get_object_or_404(Payment, paymentId=paymentId)
    if request.method == "POST":
        payment.delete()
        return redirect('payment_list')
    return render(request, 'rent_payment/payment_confirm_delete.html', {'payment': payment})
