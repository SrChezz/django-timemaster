from django.shortcuts import redirect, render
from django.http import HttpResponse  
from .models import Alarm
from .forms import AlarmForm, UpdateAlarmForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.serializers import serialize

def say_hello(request):
  return render(request, 'hello.html')

def about_us(request):
  alarms = []
  context = {'title': 'Sobre Nosotros'}
  return render(request, 'about-us.html', context) 

def view_alarms(request):
  alarms = Alarm.objects.all()
  context = {'alarms': alarms, 'title': 'Alarmas'}
  return render(request, 'alarms.html', context) 

def view_alarms_JSON(request):
    alarms = Alarm.objects.all()
    alarms_data = serialize('json', alarms)
    return JsonResponse(alarms_data, safe=False)

def view_timer(request):
  context = {'title': 'Temporizador'}
  return render(request, 'timer.html', context) 

def view_chronometer(request):
  context = {'title': 'Cronometro'}
  return render(request, 'chronometer.html', context) 

def view_pomodoro(request):
  alarms = Alarm.objects.all()
  context = {'title': 'Pomodoro'}
  return render(request, 'pomodoro.html', context) 

# @login_required(login_url='/login/')1
def create_alarm(request):
  if request.method == 'POST':
      form = AlarmForm(request.POST)
      if form.is_valid():
          form.save()
          messages.success(request, 'La alarma ha sido creada con exito')
          return redirect('home')
  else:
      form = AlarmForm()

  context = {'form': form}
  return render(request, 'alarm_form.html', context)

def update_alarm(request, pk):
  alarm = Alarm.objects.get(id=pk)

  if request.method == 'POST':
      form = AlarmForm(request.POST, instance=alarm)
      if form.is_valid():
          form.save()
          return redirect('home')
  else:
      form = AlarmForm(instance=alarm)

  context = {'form': form}
  return render(request, 'alarm_form.html', context)

@login_required(login_url='login')
def delete_alarm(request, pk):
    alarm = Alarm.objects.get(id=pk)

    if request.method == 'POST':
        alarm.delete()
        return redirect('home')
    return render(request, 'delete.html', {'obj': alarm})

def loginPage(request):
   
   if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
      user = User.objects.get(username=username);
    except:
      messages.error(request, 'El usuario no existe')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
       messages.error(request, 'User or passwrod does not exist')

   context = {}
   return render(request, 'login.html', context)

def logoutUser(request):
   logout(request)
   return redirect('login')