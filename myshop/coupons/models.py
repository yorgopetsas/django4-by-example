from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from shop.models import Product, Category, Brand
from django.contrib.auth.models import User, Group

# class Brand(models.Model):
#     pass
    # brand_name = models.CharField(max_length=50, null=True)
    # brand_visible = models.BooleanField(default=False)
    # brand_description = models.CharField(max_length=2500, default="", blank=True, null=True)
    # brand_image = models.ImageField(upload_to="uploads/brand/",  blank=True, null=True)
    # brand_title = models.CharField(max_length=100, default="", blank=True, null=True)
    # brand_url = models.URLField(blank=True, null=True)
    # brand_allowed_groups = models.ManyToManyField(User, related_name="brand_groups", blank=True)

    # def __str__(self):
    #     return str(self.brand_name)

    # class Meta:
    #     verbose_name_plural = "brands"

# class Category(models.Model):
#     name = models.CharField(max_length=50, null=True)
#     category_title = models.CharField(max_length=100, default="", blank=True, null=True)
#     category_url = models.URLField(blank=True, null=True)
#     category_visible = models.BooleanField(default=False)
#     category_parent = models.CharField(max_length=50, blank=True, null=True)
#     category_description = models.CharField(max_length=160, default="", blank=True, null=True)
#     category_allowed_groups= models.ManyToManyField(User, related_name="user_groups", blank=True)
#     category_image = models.ImageField(upload_to="uploads/category/",  blank=True, null=True)

#     def __str__(self):
#         return str(self.name)

#     class Meta:
#         verbose_name_plural = "categories"

# class Product(models.Model):
#     name = models.CharField(max_length=128)
#     short_description = models.CharField(max_length=160, default="", blank=True, null=True)
#     description = models.CharField(max_length=250000, default="", blank=True, null=True)
#     reference = models.CharField(max_length=20, default="", blank=True, null=True)
#     manufacturer_reference = models.CharField(max_length=100, default="", blank=True, null=True)
#     media = models.ImageField(upload_to="uploads/product/", null=True)
#     stock = models.IntegerField(default=0)
#     stock_min_qty_alert = models.IntegerField(default=0)
#     min_order_qty = models.IntegerField(default=1)
#     price = models.DecimalField(default=0, decimal_places=2, max_digits=7)
#     sale = models.BooleanField(default=False)
#     sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=7)
#     brand = models.OneToOneField(Brand, related_name='brand', on_delete=models.CASCADE, blank=True, null=True)
#     hashtag = models.CharField(max_length=100, default="", blank=True, null=True)
#     category = models.ManyToManyField(Category, related_name='products', blank=True)
#     dim_height = models.IntegerField(default=0)
#     dim_width = models.IntegerField(default=0)
#     dim_debt = models.IntegerField(default=0)
#     dim_weight = models.IntegerField(default=0)
#     url = models.URLField(blank=True, null=True)
#     title = models.CharField(max_length=100, default="", blank=True, null=True)
#     visible = models.BooleanField(default=False)

#     def __str__(self):
#         return str(self.name)

class Coupon(models.Model):

    DISCOUNT_CHOICES = [
        ('General', 'General'),
        ('Loyalty', 'Loyalty'),
        ('Volume', 'Volume'),
        ('Credit', 'Credit'),
        ('Product type', 'Product type'),
        ('Promotion', 'Promotion'),
    ]

    FIX_PERC_CHOICES = [
        ('Fixed', 'Fixed'),
        ('Percentage', 'Percentage'),
    ]

    discount_name = models.CharField(max_length=50, null=True)
    discount_description = models.CharField(max_length=250000, default="", blank=True, null=True)
    discount_type = models.CharField(max_length=20, choices=DISCOUNT_CHOICES, blank=True, null=True)
    discount_priority = models.IntegerField(default=0, blank=True, null=True)
    discount_code = models.CharField(max_length=20, blank=True, null=True)
    discount_active = models.BooleanField(default=False)
    discount_scope_user = models.ManyToManyField(User, related_name='users', blank=True)
    discount_scope_user_group = models.ManyToManyField(Group, related_name='groups', blank=True)
    discount_scope_product = models.ManyToManyField(Product, related_name='products', blank=True)
    discount_scope_category = models.ManyToManyField(Category, related_name='categories', blank=True)
    discount_scope_brand = models.ManyToManyField(Brand, related_name='brands', blank=True)
    discount_validity_start = models.DateTimeField()
    discount_validity_end = models.DateTimeField()
    discount_min_order_value = models.IntegerField(default=0, blank=True, null=True)
    discount_use_limit = models.IntegerField(default=0, blank=True, null=True)
    discount_use_limit_per_user = models.IntegerField(default=0, blank=True, null=True)
    discount_stop_other_discounts = models.BooleanField(default=False)
    discount_free_shipping = models.BooleanField(default=False)
    discount_fix_or_percentage = models.CharField(max_length=20, choices=FIX_PERC_CHOICES, null=True)
    discount_amount = models.IntegerField(default=0, blank=True, null=True)

    # code = models.CharField(max_length=50, unique=True)
    
    # OLD
    # valid_from = models.DateTimeField()
    # valid_to = models.DateTimeField()
    # discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],help_text='Percentage value (0 to 100)')
    # active = models.BooleanField()

    # def __str__(self):
    #     return self.code
    # END OLD

    def __str__(self):
        
        return str(self.discount_name)