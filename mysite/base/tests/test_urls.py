from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base import views

class TestUrls(SimpleTestCase):

    def test_alarms(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, views.view_alarms)
    
    def test_alarms_api(self):
        url = reverse('api-alarms')
        self.assertEquals(resolve(url).func, views.view_alarms_JSON)
    
    def test_timer(self):
        url = reverse('timer')
        self.assertEquals(resolve(url).func, views.view_timer)

    def test_chronometer(self):
        url = reverse('chronometer')
        self.assertEquals(resolve(url).func, views.view_chronometer)

    def test_pomodoro(self):
        url = reverse('pomodoro')
        self.assertEquals(resolve(url).func, views.view_pomodoro)

    def test_login(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, views.loginPage)

    def test_logout(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, views.logoutUser)

    def test_create_alarm(self):
        url = reverse('create-alarm')
        self.assertEquals(resolve(url).func, views.create_alarm)

    def test_update_alarm(self):
        url = reverse('update-alarm', args=[1])
        self.assertEquals(resolve(url).func, views.update_alarm)

    def test_delete_alarm(self):
        url = reverse('delete-alarm', args=[1])
        self.assertEquals(resolve(url).func, views.delete_alarm)
    
    def test_about_us(self):
        url = reverse('about-us')
        self.assertEquals(resolve(url).func, views.about_us)


      