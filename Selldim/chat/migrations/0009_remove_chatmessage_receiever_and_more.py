# Generated by Django 4.0 on 2022-12-01 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_alter_chatmessage_room_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='receiever',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='receiever',
        ),
    ]
