from django.contrib import admin
from timetable import  models
# Register your models here.


class TimetableAdmin(admin.ModelAdmin):
    list_per_page = 500
    list_display = ['year', 'semester', 'course_title', 'weeks', 'campus', 'place_class', 'teacher', 'teaching_class', 'assessment_method', 'course_hours',
                    'week_hours', 'total_hours', 'credit']
    ordering = ('-id',)
    search_fields = ['year', 'course_title', 'teacher']
    list_filter = (
        'year',
        'semester',
        'course_title',
        'teacher',
        'place_class',
    )

    class Meta:
        models = models.Timetable


admin.site.register(models.Timetable, TimetableAdmin)
admin.site.site_header = '校园信息查询系统'