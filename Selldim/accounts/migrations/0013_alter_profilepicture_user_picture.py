# Generated by Django 4.0 on 2022-12-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_usercomments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepicture',
            name='user_picture',
            field=models.ImageField(null=True, upload_to='profile_pictures'),
        ),
    ]
