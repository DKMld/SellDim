# Generated by Django 4.0 on 2022-11-23 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_messages_room_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='room_name',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='room_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chatmessage'),
        ),
    ]
