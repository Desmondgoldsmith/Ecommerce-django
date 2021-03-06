from django.db import models

# Create your models here.

class categories(models.Model):
    categoryName = models.CharField(max_length=50,unique=True)
    slug = models.CharField(max_length=100,unique=True)
    description = models.TextField(max_length=40,blank=True) 
    categoryImage = models.ImageField(upload_to='photos/categories', blank = True) 

# changing name for title 'category' on the admin page
    # def meta:
    #     verbose_name = 'category'
    #     verbose_name_plural = 'categories' 

    def __str___(self):
      return self.categoryName  
