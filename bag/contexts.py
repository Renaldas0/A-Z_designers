from decimal import Decimal
from django.conf import settings

"""The purpose of this 'context processor' is to make this dictionary available to all templates across the whole application"""


def bag_contents(request):

    bag_items = []
    total = 0
    product_quantity = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        # Shows user how much more they must spend to get free delivery
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_quantity': product_quantity,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
