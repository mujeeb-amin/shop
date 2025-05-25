from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=120, )
    price = models.FloatField(default=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    type = models.CharField(choices=[("for_kids", "For Kids"), 
                                     ("for_men", "For Men"), ("for_women", "For women")], 
                                     max_length=120, blank=True, null=True)
    is_published = models.BooleanField(default=True)


    def __str__(self):
        return self.title



