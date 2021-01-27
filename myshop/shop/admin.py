from django.contrib import admin
from .models import Category, Product, SubCategory, Manufacturer


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','sale_price','top','available','created','updated','manufacturer')
    list_filter = ('available','created','updated','category','manufacturer')

    list_editable = ('price','available','sale_price','top')
    prepopulated_fields = {'slug':('name',)}



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug':('name',)}


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','category','slug')
    prepopulated_fields = {'slug':('name',)}
    list_filter = ('category',)

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug':('name',)}

