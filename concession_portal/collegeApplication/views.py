from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import CollegeApplication
from railwayApplication.models import RailwayApplication
from django.core.mail import send_mail
import random
from datetime import datetime
# Create your views here.

def collegeApproved(request):
    students = CollegeApplication.objects.order_by('application_date').filter(isApproved_college=True)
    content = {
        'students': students
    }
    return render(request, 'tableApprovedCollege.html', content)

def collegePending(request):
    students = CollegeApplication.objects.order_by('application_date').filter(isApproved_college=False)
    content = {
        'students': students
    }
    return render(request, 'tablePendingCollege.html', content)


def searchApprovedCollege(request):
    content = {}
    if request.method == 'GET':
        students = CollegeApplication.objects.order_by('application_date').filter(isApproved_college=True)
        content['students'] = students
        print('get',students)
        return render(request, 'tableApprovedCollege.html', content)
    else: 
        student_id = request.POST.get('search', '')
        
        students = CollegeApplication.objects.filter(student_collegeId=student_id)
        content['students'] = students
        print('post',students) 
        return render(request, 'tableApprovedCollege.html', content)

def pendingToapproved(request, app_id):
    student = CollegeApplication.objects.get(id=app_id)
    student.isApproved_college = True 
    student.save()
    send_mail('Concession Approval',
     'Your application has been approved by the college and will be further approved by the railway',
     'hackzeroday1234@gmail.com',
     (student.student_emailId,)) 

    student_railway = RailwayApplication()
    student_railway.student_collegeId = student.student_collegeId
    student_railway.student_emailId = student.student_emailId
    student_railway.student_aadharId = student.student_aadharId
    student_railway.student_fullname = student.student_fullname
    student_railway.student_contact= student.student_contact
    student_railway.student_dob = student.student_dob
    student_railway.student_address = student.student_address
    student_railway.student_prevPassId = random.randint(100000,900000)

    # railway info 
    student_railway.source_station = student.source_station
    student_railway.destination_station = student.destination_station
    student_railway.train_class = student.train_class

    # application info 
    student_railway.isApproved_railway = False
    student_railway.application_date = student.application_date

    student_railway.save()
    return redirect('collegePending')
