# Generated by Django 5.0.4 on 2024-04-23 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0004_alter_coupon_discount_validity_end_and_more'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount_scope_category',
            field=models.ManyToManyField(blank=True, related_name='categories', to='shop.category'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount_scope_product',
            field=models.ManyToManyField(blank=True, related_name='products', to='shop.product'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
