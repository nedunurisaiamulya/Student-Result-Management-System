from multiprocessing import context

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse
from django.contrib.auth import authenticate, login
from .models import *
#from django.core.urlresolvers import reverse
from django.contrib.auth import login as auth_login
from django.test import TestCase
from .forms import SignUpForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'trial/signup.html', {'form': form})

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignUpForm)


class SuccessfulSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'john',
            'email': 'john@doe.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('index')


def sem(request, student_roll, sem):
    board = get_object_or_404(Board)
    print('currebt sem ----------------------------------------------', student_roll , sem)
    sem_marks = Marks.objects.filter(Q(student_sem__student__student_roll=student_roll) & Q(student_sem__sem__year_sem=sem))
    context = {
        'board': board,
        'roll_no':student_roll,
        'sem_marks' :sem_marks
               }
    print
    return render(request, 'trial/sem.html', context )


@login_required
def index(request):
    if request.user.student:
        return render(request, 'trial/home.html')
    return render(request, 'trial/login.html')

def myaccount(request):
    return render(request, 'trial/myaccount.html')


def test(request):
    sem_list = StudentCourse.objects.all()
    print(sem_list,'---------------------------------------------')
    return  render(request, 'trial/marks.html',{'sem_list':sem_list})