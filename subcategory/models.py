from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
# Create your models here.


class Category(MPTTModel):
    parent=TreeForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True)
    image=models.ImageField(default='default.jpg')
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by =['title']