from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Student, Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Course, CourseAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')


admin.site.register(Student, StudentAdmin)
