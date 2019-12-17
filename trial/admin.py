from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class ClassInline(admin.TabularInline):
    model = Class
    extra = 0


class DeptAdmin(admin.ModelAdmin):
    inlines = [ClassInline]
    list_display = ('name', 'dept_id')
    search_fields = ('name', 'dept_id')
    ordering = ['name']


class StudentInline(admin.TabularInline):
    model = Student
    extra = 0


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_roll', 'student_email', 'student_class', 'student_phone', 'father_name')
    search_fields = ('student_name', 'student_roll','student_class')
    ordering = ['student_name',]


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'subject_code', 'subject_credits')
    search_fields = ('subject_name', 'subject_code', 'subject_credits')
    ordering = ['subject_name',]


class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_id', 'dept',  'section')
    search_fields = ('class_id', 'dept', 'section')
    ordering = ['dept', 'section']
    inlines = [StudentInline]



class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('last_updated','board')


class PostAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'topic')


class SemAdmin(admin.ModelAdmin):
    list_display = ( 'year_sem', 'select_subject','sem_class')
    search_fields = ('year_sem','sem__class_id')
    ordering = ['year_sem', ]


class MarksInline(admin.TabularInline):
    model = Marks
    extra = 0


class StudentCourseAdmin(admin.ModelAdmin):
    inlines = [MarksInline]
    list_display = ('student', 'sem', 'cgpa')
    search_fields = ('student__student_name',  'sem__year_sem', 'student__student_class__class_id', 'student__student_class__dept__name')
    ordering = ('student__student_class__dept__name', 'student__student_class__class_id', 'student__student_roll')


admin.site.register(Sem, SemAdmin)
admin.site.register(Dept, DeptAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Subject,SubjectAdmin)
#admin.site.register(Board, BoardAdmin)
#admin.site.register(Topic, TopicAdmin)
#admin.site.register(Post, PostAdmin)
admin.site.register(StudentCourse, StudentCourseAdmin)
