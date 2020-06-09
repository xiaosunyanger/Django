from django.db import models

# Create your models here.


class News(models.Model):
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    news_title = models.CharField(
        verbose_name='新闻标题',
        max_length=200,
        blank=True,
        default=''
    )

    news_type = models.CharField(
        verbose_name='新闻类型',
        max_length=50,
        blank=True,
        default=''
    )

    news_time = models.CharField(
        verbose_name='发布日期',
        max_length=50,
        blank=True,
        default=''
    )

    news_content = models.TextField(
        verbose_name='新闻内容',
        blank=True,
        default=''
    )

    news_url = models.URLField(
        verbose_name='新闻链接',
        blank=True,
        default=''
    )

    def __str__(self):
        return str(self.news_title)

    class Meta:
        verbose_name = verbose_name_plural = '新闻系统'
