from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django_resized import ResizedImageField
from decimal import Decimal

class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=100,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

class SubCategory(models.Model):
    category = models.ForeignKey(Category,related_name='sub_category',on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=100,unique=True)

    class Meta:
        ordering = ('category',)
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'
    
    def __str__(self):
        return f"{self.category.name} > {self.name}"
    
    def get_absolute_url(self):
        return reverse('subcategory', kwargs={'slug':self.category.slug,'subslug': self.slug})


class Manufacturer(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=100,unique=True)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('', kwargs={'slug': self.slug})

class Product(models.Model):
    category = models.ForeignKey(SubCategory,related_name='products',on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer,related_name='manufacturer',on_delete=models.CASCADE,blank=True,null=True)
    
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True)
    image = ResizedImageField(size=[420, 420],upload_to=r'products/%y/%m/%d',blank=True)

    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    sale_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    top = models.BooleanField(default=False)

    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-updated','name')
        index_together = (('id','slug'),)
        verbose_name_plural = 'All products'

    @property
    def sell_price(self):
        if self.sale_price < self.price and self.sale_price>0:
            return self.sale_price
        
        return self.price

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('item_view', kwargs={'slug':self.category.category.slug,'subslug': self.category.slug,'item_slug':self.slug})
    