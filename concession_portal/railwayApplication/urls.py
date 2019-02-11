from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('pending/', views.pendingApp_railway, name='pendingApp_railway'),
    path('approved/', views.approvedApp_railway, name='approvedApp_railway'),
    path('searchApproved/', views.searchApprovedRailway, name='searchApprovedRailway'),
    path('searchPending/', views.searchPendingRailway, name='searchPendingRailway'),
    path('p2a_railway/<int:app_id>', views.pendingToapproved, name="pendingToapproved_railway")
]
