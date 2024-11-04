# Generated by Django 5.1.2 on 2024-11-04 13:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0002_customers_user_alter_customers_email'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='password',
        ),
        migrations.AlterField(
            model_name='customers',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customers',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
