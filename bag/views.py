from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view to return the contents of the shopping bag """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    shoe_size = None

    """ Products with sizes  """
    if 'product_size' in request.POST:
        size = request.POST['product_size']
        """ Shoe sizes  """
    elif 'product_shoe_size' in request.POST:
        shoe_size = request.POST['product_shoe_size']

    """ stores items in the bag even when user is still browsing"""
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'{product.name}, size : {size.upper()} has been added to your bag!')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'{product.name}, size : {size.upper()} has been added to your bag!')

    elif shoe_size:
        """ Shoe Sizes """
        if item_id in list(bag.keys()):
            if shoe_size in bag[item_id]['items_by_shoe_size'].keys():
                bag[item_id]['items_by_shoe_size'][shoe_size] += quantity
                messages.success(request, f'Updated size {shoe_size.upper()} {product.name} quantity to {bag[item_id]["items_by_shoe_size"][shoe_size]}')
            else:
                bag[item_id]['items_by_shoe_size'][shoe_size] = quantity
                messages.success(request, f'{product.name}, size : {shoe_size.upper()} has been added to your bag!')
        else:
            bag[item_id] = {'items_by_shoe_size': {shoe_size: quantity}}
            messages.success(request, f'{product.name}, size : {shoe_size.upper()} has been added to your bag!')

    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Changed {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'{product.name} has been added to your bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def edit_bag(request, item_id):
    """ Edit quantity of items selected in bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    """ stores items in the bag even when user is still browsing"""
    bag = request.session.get('bag', {})

    if size: 
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(request, f'{product.name}, size : {size.upper()} has been removed from your bag!')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Changed {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            """ Removed products """
            messages.success(request, f'{product.name} has been removed from your bag!')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove items selected in bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']

        """ stores items in the bag even when user is still browsing"""
        bag = request.session.get('bag', {})

        if size:

            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(request, f'{product.name}, size : {size.upper()} has been removed from your bag!')
        else:
            bag.pop(item_id)
            messages.success(request, f'{product.name} has been removed from your bag!')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error occurred removing item: {e}')
        return HttpResponse(status=500)
