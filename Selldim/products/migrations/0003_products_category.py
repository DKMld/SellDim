# Generated by Django 4.1.1 on 2022-10-13 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_creator_products_description_products_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
