from django.shortcuts import render
import django_filters.rest_framework
from .models import Product
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.template import RequestContext
from productpage.serializer import UserSerializer, GroupSerializer,ProductSerializer
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from .forms import DocumentForm

from django.core.paginator import Paginator

#from django.contrib.comments import Comment

def productadd(request):
    return render(request,"productproductadd/productadd.html")

def about(request):
    return render(request,"productpage/about.html")

def products(request):
    product_all = Product.objects.all()
    paginator = Paginator(product_all, 8)
    page_number = request.GET.get("page", 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'product_list': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url
    }
    return render(request,"productpage/product_page.html", context=context)

def getmyproduct(request):
    return render(request,"productpage/myproducts.html")

def productssold(request):
    return render(request,"productpage/productsold.html")
    
def productbought(request):
    return render(request,"productpage/productbought.html")
    

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
@cache_page(60 * 15)
@csrf_protect   

def getproduct(request,id):
    id=int(id)
    return render(request,"productpage/productinfo.html", context ={'id':id} )
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('id','itemname','owner', 'status','buyer')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.owner = request.user
            stock.save()
            return redirect('product')
    else:
        form = DocumentForm()
    return render(request, 'productpage/productadd.html', {
        'form': form
    })

