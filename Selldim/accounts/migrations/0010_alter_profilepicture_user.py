# Generated by Django 4.1.1 on 2022-11-15 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0009_alter_profilepicture_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepicture',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]
