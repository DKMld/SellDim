# Generated by Django 4.1.1 on 2022-11-10 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_products_slug_alter_products_category_and_more'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlikes',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='products.products'),
        ),
    ]