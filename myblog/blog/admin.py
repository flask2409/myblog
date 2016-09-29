from django.contrib import admin
from .models import Post,Category

class ModelPost(admin.ModelAdmin):
    list_display = ('title', 'body', 'date','category', 'published')
    search_fields = ['title']


admin.site.register(Post, ModelPost)
admin.site.register(Category)
