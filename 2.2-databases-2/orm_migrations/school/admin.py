from django.contrib import admin

from .models import Student, Teacher, StudentTeacher


class StudentTeacherInline(admin.TabularInline):
    model = StudentTeacher
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'group',)
    list_editable = ('group', )
    search_fields = ('group',)
    list_filter = ('teacher',)
    empty_value_display = '-пусто-'
    inlines = [StudentTeacherInline]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'subject',)
    list_editable = ('subject',)
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'




