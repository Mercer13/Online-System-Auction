from django.urls import path, include
from productpage import views
from rest_framework import routers
#from productpage.feeds import DreamrealCommentsFeed
from django.conf.urls import url


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('products', views.ProductViewSet)

urlpatterns = [
    path('', views.products, name='product'),
    path("<int:id>/", views.getproduct, name="get_product"),
    path("rest/", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('myproducts/', views.getmyproduct, name="my_product"),
    path('productssold/', views.productssold, name="products_sold"),
    path('productbought/', views.productbought, name="product_bought"),
    path('uploadproduct/', views.model_form_upload, name="upload_product")
]
