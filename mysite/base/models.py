from django.db import models
import ast

# Create your models here.
class Alarm(models.Model):
  title = models.CharField(max_length=100)
  time = models.TimeField()
  active = models.BooleanField(default=True, null=True)
  days_of_week = models.CharField(max_length=50, null=True)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-updated',  '-created']  
  def __str__(self):
      return self.title

  @property
  def days_of_week_list(self):
    if self.days_of_week:
        try:
            return ast.literal_eval(self.days_of_week)
        except (SyntaxError, ValueError):
            # Handle the case where self.days_of_week is not a valid Python literal
            return []
    return []

