from django.contrib import admin
from .models import Category,Service

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Category,CategoryAdmin)

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('title', 'author', 'published')
    search_fields=('title', 'content', 'author__username', 'category__name')
    date_hierarchy='published'
    list_filter=('author__username', 'category__name')
admin.site.register(Service,ServiceAdmin)

