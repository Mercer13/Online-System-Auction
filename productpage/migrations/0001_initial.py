# Generated by Django 3.0.6 on 2020-05-30 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import productpage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=200, verbose_name='Назва товару: ')),
                ('description', models.CharField(max_length=200, verbose_name='Опис: ')),
                ('image', models.ImageField(default='bg3.jpg', upload_to=productpage.models.user_directory_path, verbose_name='Зображення: ')),
                ('initialbid', models.IntegerField(validators=[productpage.models.validate_even], verbose_name='Початкова ставка: ')),
                ('status', models.IntegerField(default=0)),
                ('buyer', models.CharField(blank=True, max_length=200, null=True)),
                ('bid', models.IntegerField(blank=True, default=0)),
                ('createddate', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-createddate'],
            },
        ),
    ]
