from django.shortcuts import render, get_object_or_404
# 引入BlogArticles类
from .models import BlogArticles


# Create your views here.
# 获取文章标题
def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog/titles.html", {"blogs": blogs})


# 获取文档内容
def blog_article(request, article_id):
    article = BlogArticles.objects.get(id=article_id)
    pub = article.publish
    return render(request, "blog/content.html", {"article": article, "publish": pub})

