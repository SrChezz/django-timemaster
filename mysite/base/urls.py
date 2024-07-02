from django.urls import path
from . import views

urlpatterns = [
  path('', views.view_alarms, name="home"),
  path('api/alarms/', views.view_alarms_JSON, name="api-alarms"),
  path('hello/', views.say_hello, name="hello"),
  path('timer', views.view_timer, name="timer"),
  path('chronometer', views.view_chronometer, name="chronometer"), 
  path('pomodoro', views.view_pomodoro, name="pomodoro"),
  path('login/', views.loginPage, name="login"),
  path('logout/', views.logoutUser, name="logout"),
  path('create-alarm/', views.create_alarm, name="create-alarm"),
  path('update-alarm/<str:pk>/', views.update_alarm, name="update-alarm"),
  path('delete-alarm/<str:pk>/', views.delete_alarm, name="delete-alarm"),
  path('about-us/', views.about_us, name="about-us")
]