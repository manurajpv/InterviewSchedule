from django.urls import path
from . import views


urlpatterns =[
  path('',views.home,name='index'),
  path('register/',views.register,name='register'),
  path('interviewerRegister/',views.interviewerRegister, name='interviewerRegister'),
  path('candidateRegister/',views.RegisterCandidate, name="candidateRegister"),
  path('HR/',views.HR,name='HR_Dashboard'),
  path('checkSchedule/', views.checkSchedule, name="checkSchedule")
  ]