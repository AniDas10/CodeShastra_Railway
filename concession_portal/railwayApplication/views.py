from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RailwayApplication
from django.core.mail import send_mail
import random
# Create your views here.
def pendingApp_railway(request):
    students = RailwayApplication.objects.order_by('application_date').filter(isApproved_railway=False)
    content = {
        'students':students
    }
    return render(request, 'tablePendingRailway.html', content)

def approvedApp_railway(request):
    students = RailwayApplication.objects.order_by('application_date').filter(isApproved_railway=True)
    content = {
        'students': students
    }
    return render(request, 'tableApprovedRailway.html', content)

def searchApprovedRailway(request):
    content = {}
    if request.method == 'GET':
        students = RailwayApplication.objects.order_by('application_date').filter(isApproved_railway=True)
        content['students'] = students
        return render(request, 'tableApprovedRailway.html', content)
    else: 
        student_id = request.POST.get('search', '')
        students = RailwayApplication.objects.order_by('application_date').filter(student_aadharId=student_id, isApproved_railway=True)
        content['students'] = students 
        return render(request, 'tableApprovedRailway.html', content)

def searchPendingRailway(request):
    content = {}
    if request.method == 'GET':
        students = RailwayApplication.objects.order_by('application_date').filter(isApproved_railway=False)
        content['students'] = students
        return render(request, 'tablePendingRailway.html', content)
    else: 
        student_id = request.POST.get('search', '')
        students = RailwayApplication.objects.order_by('application_date').filter(student_collegeId=student_id, isApproved_railway=False)
        content['students'] = students 
        return render(request, 'tablePendingRailway.html', content)

def pendingToapproved(request, app_id):
    student = RailwayApplication.objects.get(id=app_id)
    student.isApproved_railway = True 
    student.save() 
    unique_id = str(random.randint(1000000, 9000000)) + str(random.randint(1000000, 9000000)) 
    send_mail(
        'Application Approval By Railway',
        'Your application has been approved by railway and please use this unique Id to collect your pass: ' + unique_id,
        'hackerzeroday123@gmail.com',
        (student.student_emailId,)
    )
    return redirect('pendingApp_railway')