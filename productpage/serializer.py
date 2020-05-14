from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Product
 
     
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields=('id','image','itemname','description','initialbid','createddate','owner','status','buyer','bid')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')