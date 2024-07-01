from django.contrib import admin
from .models import Articles




class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'actif', 'slug', 'image']

admin.site.register(Articles, ArticleAdmin)
