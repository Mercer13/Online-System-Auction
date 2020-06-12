from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError

# Create your models here.

def chop_microseconds(delta):
    return delta - timedelta(microseconds=delta.microseconds)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    #ext = filename.split('.')[-1]
    return '{0}/{1}'.format(instance.pk,filename)

def validate_even(value):
    if value > 999999:
        raise ValidationError('Занадто велика ціна!')    

class Category(models.Model):
    category_name = models.CharField("Категория", max_length=150)
    url = models.SlugField(max_length=160, unique=True)
    # object = models.manager()

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Product(models.Model):
    itemname = models.CharField(verbose_name="Назва товару: ", null=False,max_length=200)
    description = models.CharField(verbose_name="Опис: ", null=False,max_length=200)
    image = models.ImageField(verbose_name="Зображення: ", upload_to=user_directory_path, default="bg3.jpg")
    initialbid = models.IntegerField(verbose_name="Початкова ставка: ", null=False, validators=[validate_even])
    owner = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    buyer = models.CharField(blank=True,null=True,max_length=200)
    bid = models.IntegerField(default=0,blank=True)
    createddate = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.itemname    

    class Meta:
        ordering = ['-createddate']

