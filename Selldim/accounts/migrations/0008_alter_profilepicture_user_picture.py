# Generated by Django 4.1.1 on 2022-11-13 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepicture',
            name='user_picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]