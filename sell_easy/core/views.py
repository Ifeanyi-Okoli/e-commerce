from django.shortcuts import render
from django.http import HttpResponse
from .models import Products, Store, Category

# Create your views here.


# def web_page(products):
#     page = "<url>"
#     for product in products:
#         page += f"""<li><h1>{product["name"]}</h1><h2>{product["desc"]}</h2><p>{product["price"]}</p></li>"""
        
#     page+= "</ul>"
#     return page

# def store_page(products):
#     page = "<url>"
#     for store in stores:
#         page += f"<li><h1>{store.name}</h1><h2>{store.tagline}</h2><p>{store.owner.username}, Welcome</p></li>"
        
#     page+= "</ul>"
#     return page


def products(request):
    products = Products.objects.all().values()
    categories = Category.objects.all().values()
    # webpage = web_page(products)
    context = {"products": products, "categories": categories}
    return render(request, "core/products.html", context)

# def product(request, id):
#     product = Products.objects.filter(id=id).values()
#     webpage = web_page(product)
#     return HttpResponse(webpage)

def product(request, id):
    product = Products.objects.get(id=id)
    # related_products = product.objects.filter(category=product.category).exclude(id=id)
    # webpage = web_page(product)
    return render(request, 'core/detail.html', {'product': product})

def stores(request):
    stores = Store.objects.all().values()
    # return HttpResponse(store_page(stores))

def store(request, id):
    store = Store.objects.filter(id=id).values()
    # webpage = web_page(store)
    # return HttpResponse(webpage)

def store_products(request, id):
    store_products = Products.objects.filter(id=id).values()
    # webpage = web_page(store_products)
    # return HttpResponse(webpage)

def categories(request):
    categories = Category.objects.all().values()
    # webpage = web_page(categories)
    # return HttpResponse(webpage)

def category(request, id):
    category = Category.objects.filter(id=id).values()
    # webpage = web_page(category)
    # return HttpResponse(webpage)