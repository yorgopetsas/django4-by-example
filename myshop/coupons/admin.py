from django.contrib import admin
from .models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    # pass
    list_display = ['discount_name', 'discount_active', 'discount_amount', 'discount_validity_start', 'discount_validity_end']
    list_filter = ['discount_active', 'discount_validity_start', 'discount_validity_end']
    search_fields = ['discount_code']
    # filter_horizontal = ['discount_scope_product', 'discount_scope_category', 'discount_scope_brand']

    class Media:
            js = ('your_app/js/custom_admin.js',)