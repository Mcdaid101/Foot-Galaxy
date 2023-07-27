from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from products.models import Product
from django.contrib import messages
# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += 1
    else:
        bag[item_id] = 1

    messages.success(request, f'You added {product.name} to your bag')
    request.session['bag'] = bag
    return redirect(redirect_url)
