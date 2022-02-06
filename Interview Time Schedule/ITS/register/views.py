from multiprocessing import context
from tracemalloc import start
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timedelta
import json


from interviewers.models import Interviewer
from candidates.models import Candidate


def home(request):
  return render(request,'home.html')

def register(request):
  return render(request,'register.html')

def interviewerRegister(request):
  print(request.POST['name'])
  print(request.POST['id'])
  print(request.POST['date'])
  print(request.POST['start_time'])
  print(request.POST['end_time'])
  try:
    Interviewer.objects.create(user_id=str(request.POST['id']),
      name= str(request.POST['name']),
      start_time= str(datetime.strptime(str(request.POST['date'])+" "+ str(request.POST['start_time']), "%m/%d/%Y %H:%M")),
      end_time= str(datetime.strptime(str(request.POST['date'])+" "+ str(request.POST['end_time']), "%m/%d/%Y %H:%M"))
    )
  except Exception as e:
    print(e)
    context = {'error': e , 'result': False}
    return render(request, 'register.html',context)
  else:
    context = {'result' : True}
    return render(request, 'submitted.html',context)


def interviewerRegister(request):
  print(request.POST['name'])
  print(request.POST['id'])
  print(request.POST['date'])
  print(request.POST['start_time'])
  print(request.POST['end_time'])
  try:
    Interviewer.objects.create(user_id=str(request.POST['id']),
      name= str(request.POST['name']),
      start_time= str(datetime.strptime(str(request.POST['date'])+" "+ str(request.POST['start_time']), "%m/%d/%Y %H:%M")),
      end_time= str(datetime.strptime(str(request.POST['date'])+" "+ str(request.POST['end_time']), "%m/%d/%Y %H:%M"))
    )
  except Exception as e:
    print(e)
    context = {'error': e , 'result': False}
    return render(request, 'register.html',context)
  else:
    context = {'result' : True}
    return render(request, 'submitted.html',context)

def RegisterCandidate(request):
  print(request.POST['name'])
  print(request.POST['id'])
  print(request.POST['date'])
  print(request.POST['start_time'])
  print(request.POST['end_time'])
  try:
    Candidate.objects.create(user_id=str(request.POST['id']),
      name= str(request.POST['name']),
      start_time= str(datetime.strptime(str(request.POST['date'])+" "+ str(request.POST['start_time']), "%m/%d/%Y %H:%M")),
      end_time= str(datetime.strptime(str(request.POST['date'])+" "+ str(request.POST['end_time']), "%m/%d/%Y %H:%M"))
    )
  except Exception as e:
    print(e)
    context = {'error': e , 'result': False}
    return render(request, 'register.html',context)
  else:
    context = {'result' : True}
    return render(request, 'submitted.html',context)

def HR(request):
  return render(request,'HR_dashboard.html')

def checkSchedule(request):
  print(request.POST['candidate_id'])
  print(request.POST['interviewer_id'])
  try:
    interviewer = Interviewer.objects.get(user_id=request.POST['interviewer_id'])
    candidate = Candidate.objects.get(user_id=request.POST['candidate_id'])
  except Exception as e:
    print(e)
    return JsonResponse({'result': False,'Notfound':True})
    
  else:
    in_time_start = interviewer.start_time
    can_time_start = candidate.start_time
    in_time_end = interviewer.end_time
    can_time_end = candidate.end_time
    print(in_time_start)
    print(can_time_start)
    print(in_time_end)
    print(can_time_end)
    if ((in_time_end<=can_time_start) or (can_time_end<=in_time_start)):
      print('no available')
      return JsonResponse({'result' : False, 'availability':True})
    start = in_time_start if can_time_start < in_time_start else can_time_start
    end = in_time_end if can_time_end > in_time_end else can_time_end
    schedule =[]
    print(start)
    print(end)
    while(start<end):
      print(start, start+timedelta(hours=1))
      schedule.append(start)
      start = start+timedelta(hours=1)
    print(schedule)

    return JsonResponse({'result' : True , 'schedule':schedule, 'candidate': candidate.name, 'interviewer':interviewer.name})
