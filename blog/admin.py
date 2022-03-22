from django.contrib import admin

# 引入BlogArticles类
from .models import BlogArticles


class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish")
    list_filter = ("publish", "author")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ['publish', 'author']


# 注册BlogArticles类到admin
admin.site.register(BlogArticles, BlogArticlesAdmin)
