from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('approved/', views.collegeApproved, name='collegeApproved'),
    path('pending/', views.collegePending, name='collegePending'),
    path('searchApproved/', views.searchApprovedCollege, name='searchApprovedCollege'),
    path('p2a_college/<int:app_id>', views.pendingToapproved, name="pendingToapproved"),
]