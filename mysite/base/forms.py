# from django.forms import ModelForm
from .models import Alarm
from django import forms
from django.forms import ModelForm

class UpdateAlarmForm(ModelForm):
  class Meta:
    model = Alarm
    fields = ['title', 'time', 'active', 'days_of_week']

class AlarmForm(forms.ModelForm):
  class Meta:
      model = Alarm
      fields = ['title', 'time', 'active', 'days_of_week']

  time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
  days_of_week = forms.MultipleChoiceField(
      choices=[
          ('Lun', 'Lunes'),
          ('Mar', 'Martes'),
          ('Mierc', 'Miercoles'),
          ('Juev', 'Jueves'),
          ('Vier', 'Viernes'),
          ('Sab', 'Sabado'),
          ('Dom', 'Domingo'),
      ],
      widget=forms.CheckboxSelectMultiple,
  )
