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
#from django.contrib.comments import Comment

def productadd(request):
    return render(request,"productproductadd/productadd.html")

def products(request):
    return render(request,"productpage/product_page.html")

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
    context={
        'id':id
    }
    return render(request,"productpage/productinfo.html",context)
    
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

