from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MXUXPIEQO5wDvJsm0Us8BJCUnm55IrWyHOYagItPUXhuLebkwADxohdG3s7sb7efchPHPKFrbTiNx2h151FPjfO00i7QQl41f',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
