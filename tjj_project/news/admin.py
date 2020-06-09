from django.contrib import admin
from news import models

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_per_page = 500
    list_display = ['news_time', 'news_title', 'news_type', 'news_url']
    ordering = ('-id', )
    search_fields = ['news_time', 'news_title', 'news_type']
    list_filter = (
        'news_time',
        'news_type',
    )

    class Meta:
        models = models.News


admin.site.register(models.News, NewsAdmin)
