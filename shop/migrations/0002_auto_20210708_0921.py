# Generated by Django 3.1.8 on 2021-07-08 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='shop',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='about_product', to='shop.shop', verbose_name='Магазин'),
        ),
        migrations.AlterField(
            model_name='productparameter',
            name='parameter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='parameter_name', to='shop.parameter', verbose_name='Название параметра'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_shop', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
