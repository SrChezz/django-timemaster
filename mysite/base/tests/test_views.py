from django.test import TestCase, Client
from django.urls import reverse
from base.models import Alarm
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.alarm = Alarm()
        self.alarm_url = reverse('home')
        self.create_alarm = reverse('create-alarm')
        self.delete_alarm = reverse('delete-alarm', args=[id==1])
        self.update_alarm = reverse('update-alarm', args=[id==1])
        self.my_alarm = {
            'title': 'Test Alarma',
            'time': '12:00',
            'active': True,
            'days_of_week': ['Lun', 'Mar']
        }
    
    def test_alarms_get(self):
        response = self.client.get(self.alarm_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alarms.html')
        self.assertTemplateUsed(response, 'components/main.html')
        self.assertTemplateUsed(response, 'components/navbar.html')
        self.assertTemplateUsed(response, 'components/sidebar.html')
        self.assertTemplateUsed(response, 'components/footer.html')

    def test_alarms_post(self):
        response = self.client.post(self.create_alarm, self.my_alarm)

        self.assertEqual(response.status_code, 302)
        print(self.my_alarm)
        self.assertEqual(self.my_alarm['title'], 'Test Alarma')

    def test_alarms_delete(self):
        response = self.client.delete(self.delete_alarm, json.dumps({
            'id': 1
        }))

        self.assertEqual(response.status_code, 302)

    def test_alarms_update(self):
        create_response = self.client.post(self.create_alarm, self.my_alarm)
        self.assertEqual(create_response.status_code, 302)
        alarm = Alarm.objects.get(title='Test Alarma')

        updated_data = {
            'title': 'Test Updated',
            'time': '12:00',
            'active': True,
            'days_of_week': ['Lun', 'Mar']
        }
        update_response = self.client.post(reverse('update-alarm', args=[alarm.id]), updated_data)

        self.assertEqual(update_response.status_code, 302)
        alarm.refresh_from_db()
        self.assertEqual(alarm.title, 'Test Updated')

        