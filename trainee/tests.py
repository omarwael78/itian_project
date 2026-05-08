from django.urls import reverse
from django.test import TestCase

from .models import Trainee


class TraineeViewsTest(TestCase):
    def setUp(self):
        self.trainee_a = Trainee.objects.create(name='Alice', track='Django')
        self.trainee_b = Trainee.objects.create(name='Bob', track='React')

    def test_trainee_list_returns_200_and_shows_all_trainees(self):
        url = reverse('trainee_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.trainee_a.name)
        self.assertContains(response, self.trainee_a.track)
        self.assertContains(response, self.trainee_b.name)
        self.assertContains(response, self.trainee_b.track)

    def test_trainee_detail_returns_200_for_existing_trainee(self):
        url = reverse('trainee_detail', args=[self.trainee_a.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.trainee_a.name)
        self.assertContains(response, self.trainee_a.track)

    def test_trainee_detail_returns_404_for_missing_trainee(self):
        missing_id = self.trainee_b.id + 999
        url = reverse('trainee_detail', args=[missing_id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_add_trainee_post_creates_new_trainee_and_redirects(self):
        url = reverse('add_trainee')
        response = self.client.post(url, data={'name': 'Charlie', 'track': 'Python'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Trainee.objects.count(), 3)
        self.assertTrue(Trainee.objects.filter(name='Charlie', track='Python').exists())
        self.assertEqual(response.url, reverse('trainee_list'))

    def test_delete_trainee_removes_record_and_redirects(self):
        url = reverse('delete_trainee', args=[self.trainee_b.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Trainee.objects.filter(id=self.trainee_b.id).exists())
        self.assertEqual(response.url, reverse('trainee_list'))
