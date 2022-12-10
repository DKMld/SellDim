# Generated by Django 4.0 on 2022-11-23 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_remove_chatmessage_message_remove_chatmessage_sender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='room_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chatmessage', unique=True),
        ),
    ]