# Generated by Django 4.1 on 2022-08-13 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(blank=True, default='defaults/tr.png', null=True, upload_to='product/'),
        ),
    ]
