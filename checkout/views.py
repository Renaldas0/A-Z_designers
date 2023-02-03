from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MXUXPIEQO5wDvJsm0Us8BJCUnm55IrWyHOYagItPUXhuLebkwADxohdG3s7sb7efchPHPKFrbTiNx2h151FPjfO00i7QQl41f',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
