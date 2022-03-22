from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
# 继承django.db.models.Model类
class BlogArticles(models.Model):
    # 定义属性，每个属性对应将来数据库表中的一个字段
    title = models.CharField(max_length=300)
    # 定义博客文章与用户之间的关系，ForeignKey反应了一对多的关系，类User就是BlogArticles的对应对象，related_name的作用就是允许通过类User反向查询到BlogArticles
    # on_delete 删除User数据后，博客文章表不删除
    author = models.ForeignKey(User, related_name="blog_posts", on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    # 定义BlogArticles实例对象的显示顺序，按照publish字段的倒叙显示
    class Meta:
        # 定义类类在django admin web端显示的名称，如果不定义会自动在类名后面加s
        verbose_name_plural = "Blog Articles"
        ordering = ("-publish",)

    # 通过__str__()函数打印title
    def __str__(self):
        return self.title
