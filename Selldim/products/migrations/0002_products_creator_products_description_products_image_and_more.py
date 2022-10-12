# Generated by Django 4.1.1 on 2022-10-12 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='product_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]