from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator
from .models import Order

def index(request):
    product_objects = Products.objects.all()

    # Filter products based on the search query (Search Code)
    item_name = request.GET.get('item_name')
    if item_name:
        product_objects = product_objects.filter(title__icontains=item_name)
    
     
    #Paginator Code
    paginator = Paginator(product_objects, 4) # Show 4 products per page
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)


    return render(request, 'shop/index.html', {'product_objects': product_objects})


def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_object': product_object})


def checkout(request):

    if request.method == 'POST':
        # Get the form data
        items = request.POST.get('items',"")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        address2 = request.POST.get('address2',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"") 
        ccname = request.POST.get('ccname', "")
        ccnumber = request.POST.get('ccnumber', "")
        expiration = request.POST.get('expiration', "")
        cvv = request.POST.get('cvv', "")

        # Create an instance of the Order model
        order = Order(
            items=items,
            name=name,
            email=email,
            address=address,
            address2=address2,
            city=city,
            state=state,
            zipcode=zipcode,
            total=total,
            ccname=ccname,
            ccnumber=ccnumber,
            expiration=expiration,
            cvv=cvv
        )

        order.save()

    return render(request,'shop/checkout.html')

def custom_404_view(request, exception):
    return render(request, 'shop/404.html', status=404)