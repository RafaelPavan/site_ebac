from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("tittle", "slug", "status", "created_on")
    list_filter = ("status",)
    search_fields = ["tittle", "content"]
    prepopulated_fields = {"slug": ("tittle",)}

admin.site.register(Post, PostAdmin)