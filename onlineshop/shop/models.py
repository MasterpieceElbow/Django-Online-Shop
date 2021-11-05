from django.db import models
from django.urls import reverse
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(blank=True,
                              upload_to='category/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:list_by_category', args=[self.slug])

    def get_products_count(self):
        return self.products.count()


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(blank=True,
                              upload_to='products/%Y/%m/%d/')
    available = models.BooleanField(default=True)
    sold = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        index_together = (('name', 'slug'), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])


class Review(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='reviews')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='reviews')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
