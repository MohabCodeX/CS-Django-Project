from django.shortcuts import render
from .models import Products
import locale
from django.core.paginator import Paginator

def index(request):
    product_objects = Products.objects.all()

    # Filter products based on the search query (Search Code)
    item_name = request.GET.get('item_name')
    if item_name:
        product_objects = product_objects.filter(title__icontains=item_name)
    
    # Format prices with thousands separators and without decimal places
    locale.setlocale(locale.LC_ALL, '')  # Use the default locale
    for product in product_objects:
        product.formatted_price = locale.format_string("%.0f", product.price, grouping=True)
     
    #Paginator Code
    paginator = Paginator(product_objects, 4) # Show 4 products per page
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)


    return render(request, 'shop/index.html', {'product_objects': product_objects})


def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_object': product_object})