from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin
from .models import Category


class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        
        return qs

   
admin.site.register(Category,CategoryAdmin)