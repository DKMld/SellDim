# Generated by Django 4.0 on 2022-11-23 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('chat', '0006_alter_chatmessage_room_name_alter_messages_room_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='receiever',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_user', to='auth.user'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_user', to='auth.user'),
        ),
    ]
