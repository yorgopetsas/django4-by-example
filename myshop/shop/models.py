from django.db import models
from django.urls import reverse

class Brand(models.Model):
    # pass
    brand_name = models.CharField(max_length=50, null=True)
    # brand_visible = models.BooleanField(default=False)
    # brand_description = models.CharField(max_length=2500, default="", blank=True, null=True)
    # brand_image = models.ImageField(upload_to="uploads/brand/",  blank=True, null=True)
    # brand_title = models.CharField(max_length=100, default="", blank=True, null=True)
    # brand_url = models.URLField(blank=True, null=True)
    # brand_allowed_groups = models.ManyToManyField(User, related_name="brand_groups", blank=True)

    def __str__(self):
        return str(self.brand_name)

    # class Meta:
    #     verbose_name_plural = "brands"

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name']),]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    sku = models.CharField(max_length=20)

    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['id', 'slug']), models.Index(fields=['name']), models.Index(fields=['-created']),]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])