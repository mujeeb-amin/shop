from django.contrib import admin

# Register your models here.
from products.models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["title", "price","type", "category", "updated_date", "is_published"]
    list_display_links = ["title", 'price']
    list_editable = ["is_published"]
    list_filter = ["category", "is_published"]
    search_fields = ["title", "price"]
    readonly_fields = ["created_date", "updated_date"]
    # list_per_page = 2
    fields = ["title", "price","type", "category", "is_published", "created_date", "updated_date"]
    


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)