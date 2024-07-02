from django.test import TestCase
from base.models import Alarm

class TestModels(TestCase):
    
    def setUp(self):
        self.my_alarm = Alarm.objects.create(
            title='Test Alarma',
            # active=True,
            time='12:00',
            days_of_week=['Lun', 'Mar']
        )

    def test_active_on_creation(self):
        self.assertEquals(self.my_alarm.active, True)
