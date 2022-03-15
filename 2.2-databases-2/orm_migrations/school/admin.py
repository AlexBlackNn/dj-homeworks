from django.contrib import admin

from .models import Student, Teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'group',)
    list_editable = ('group', )
    search_fields = ('group',)
    list_filter = ('teacher',)
    empty_value_display = '-пусто-'

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'subject',)
    list_editable = ('subject',)
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'




