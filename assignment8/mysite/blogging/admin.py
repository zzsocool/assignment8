from django.contrib import admin
from blogging.models import Post
from blogging.models import Category

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class CategoryAdmin(admin.ModelAdmin):
    exclude =('post',)

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
# Register your models here.
