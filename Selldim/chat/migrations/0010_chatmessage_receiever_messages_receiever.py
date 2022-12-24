# Generated by Django 4.0 on 2022-12-02 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('chat', '0009_remove_chatmessage_receiever_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='receiever',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_user', to='auth.user'),
        ),
        migrations.AddField(
            model_name='messages',
            name='receiever',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiever', to='auth.user'),
        ),
    ]
