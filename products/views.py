from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Brand, League
from django.urls import reverse
from django.db.models.functions import Lower


# Create your views here.
def all_products(request):

    products = Product.objects.all()
    query = None
    categories = None
    brands = None
    leagues = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
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

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_brands': brands,
        'current_leagues': leagues,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def get(self, request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    sort_by = request.GET.get("sort", "l2h")
    if sort_by == "l2h":
        products = product.products.order_by("price")
    elif sort_by == "h2l":
        products = product.products.order_by("-price")

    product_list = products.objects.all()
    return render(request, 'products/products.html', {"product": products, 'product_list': product_list,})

    
