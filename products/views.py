from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Brand, League
from django.urls import reverse
from django.db.models.functions import Lower
from .forms import ProductForm


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    query = None
    categories = None
    brands = None
    leagues = None
    sort_by = request.GET.get('sort_by', 'name')

    if sort_by == 'name':
        products = Product.objects.all().order_by('name')  # Sort alphabetically by name
    elif sort_by == '-name':
        products = Product.objects.all().order_by('-name')  # Sort by ascending price
    elif sort_by == 'price_asc':
        products = Product.objects.all().order_by('price')  # Sort by ascending price
    elif sort_by == 'price_desc':
        products = Product.objects.all().order_by('-price')  # Sort by descending price
    else:
        products = Product.objects.all().order_by('name')  # Default products

    if request.GET:  
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
  
        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            products = products.filter(brand__name__in=brands)
            brands = Brand.objects.filter(name__in=brands)
        
        if 'league' in request.GET:
            leagues = request.GET['league'].split(',')
            products = products.filter(league__name__in=leagues)
            leagues = League.objects.filter(name__in=leagues)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(desc__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_brands': brands,
        'current_leagues': leagues,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)