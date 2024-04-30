from django.contrib import admin
from .models import Category, Product, Brand
from orders.models import Order, OrderItem
# from django.utils.safestring import mark_safe
from coupons.models import Brand

import csv
import datetime
from django.http import HttpResponse

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = f'attachment; filename={opts.verbose_name}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
    for field in fields:
        value = getattr(obj, field.name)
        if isinstance(value, datetime.datetime):
            value = value.strftime('%d/%m/%Y')
        data_row.append(value)
    writer.writerow(data_row)
    return response

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'sku', 'available', 'category', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'sku']
    raw_id_fields = ['category']
    # date_hierarchy = ['created']
    ordering = ['price', 'available','sku']
    actions = [export_to_csv]

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


export_to_csv.short_description = 'Export to CSV'

@admin.register(Order)    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand_name']