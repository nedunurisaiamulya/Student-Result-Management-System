from django.db import models
from datetime import datetime
from django.urls import reverse
from phone_field import PhoneField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
#username:amulya pswd:a
#student_username:sai, pswd:project231
select_gender = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)
select_year =(
    ('1-1','1-1'),
    ('1-2','1-2'),
    ('2-1','2-1'),
    ('2-2','2-2'),
    ('3-1','3-1'),
    ('3-2','3-2'),
    ('4-1','4-1'),
    ('4-2','4-2'),
)
select_credit = (
        ('O(Outstanding)', 'O(Outstanding)'),
        ('A+(Excellent)', 'A+(Excellent)'),
        ('A(Very Good)','A(Very Good)'),
        ('B+(Good)', 'B+(Good)'),
        ('B(Average)', 'B(Average)'),
        ('C(Pass)', 'C(Pass)'),
        ('F(Fail)', 'F(Fail)'),
        ('AB(Absent)', 'AB(Absent)')
    )


class Dept(models.Model):
    dept_id = models.IntegerField(null = False)
    name = models.CharField(primary_key=True, max_length=200)

    def __str__(self):
        return self.name


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=20, null=False)
    subject_creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    subject_credits = models.IntegerField(null = False, default=2)

    def __str__(self):
        return self.subject_name

    def get_absolute_url(self):
        return reverse('subjects:subject_list')


class Class(models.Model):
    class_id = models.CharField(primary_key='False', max_length=100, null=False)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    section = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('student_classes:class_list')

    def __str__(self):
        return "%s "%(self.class_id)


class Sem(models.Model):
    year_sem = models.CharField(max_length=8, choices=select_year)
    select_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    sem_class = models.ForeignKey(Class, on_delete=models.CASCADE, default= '16CSEA')
    def __str__(self):
        return  self.year_sem

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    student_name = models.CharField(max_length=100)
    student_roll = models.CharField(max_length=10, unique=True)
    student_email = models.EmailField()
    student_gender = models.CharField(max_length=8, choices=select_gender)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE, default=True, null=False)
    student_date_of_birth = models.DateField(default= datetime.now, blank=True)
    student_phone =PhoneField(blank=True, help_text='Contact phone number')
    father_name = models.CharField(max_length=20, null=True)
    mother_name = models.CharField(max_length=20, null=True)
    parent_phone = PhoneField(blank=True, help_text='Contact phone number')
    student_reg = models.DateField(auto_now_add=True, auto_now=False)

    def get_absolute_url(self):
        return reverse('students:student_create')

    def __str__(self):
        return self.student_name


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts',on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+',on_delete=models.CASCADE)


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    sem = models.ForeignKey(Sem, on_delete=models.CASCADE)
    cgpa = models.FloatField(default=6.5)

    def __str__(self):
        return "%s Sem-%s " % (self.student, self.sem)
    class Meta:
        ordering = ['sem']

class Marks(models.Model):
    student_sem = models.ForeignKey(StudentCourse, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.CharField(choices=select_credit, max_length=20)

    class Meta:
        ordering = ['-student_sem__sem']

