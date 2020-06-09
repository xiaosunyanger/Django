from django.db import models

# Create your models here.


class Timetable(models.Model):
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    year = models.CharField(
        verbose_name='学年',
        max_length=100,
        blank=True,
        default=''
    )

    semester = models.IntegerField(
        verbose_name='学期',
        blank=True,
        null=True
    )

    course_title = models.CharField(
        verbose_name='课程名称',
        max_length=100,
        blank=True,
        default=''
    )

    weeks = models.CharField(
        verbose_name='周数',
        max_length=50,
        blank=True,
        default=''
    )

    campus = models.CharField(
        verbose_name='校区',
        max_length=50,
        blank=True,
        default=''
    )

    place_class = models.CharField(
        verbose_name='上课地点',
        max_length=50,
        blank=True,
        default=''
    )

    teacher = models.CharField(
        verbose_name='教师',
        max_length=50,
        blank=True,
        default=''
    )

    teaching_class = models.CharField(
        verbose_name='教学班',
        max_length=50,
        blank=True,
        default=''
    )

    assessment_method = models.CharField(
        verbose_name='考核方式',
        max_length=50,
        blank=True,
        default=''
    )

    course_hours = models.CharField(
        verbose_name='课程学时组成',
        max_length=50,
        blank=True,
        default=''
    )

    week_hours = models.CharField(
        verbose_name='周学时',
        max_length=50,
        blank=True,
        default=''
    )

    total_hours = models.CharField(
        verbose_name='总学时',
        max_length=50,
        blank=True,
        default=''
    )

    credit = models.CharField(
        verbose_name='学分',
        max_length=50,
        blank=True,
        default=''
    )

    def __str__(self):
        return str(self.course_title)

    class Meta:
        verbose_name = verbose_name_plural = '课表系统'
