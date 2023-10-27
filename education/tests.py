from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test11@test.ru',
            password='12qw34er',
            is_active=True
        )

        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title='test1',
            owner=self.user
        )

        self.lesson = Lesson.objects.create(
            title='test1',
            course=self.course,
            owner=self.user
        )

    def test_lesson_list(self):
        """Тест вывода списка уроков"""
        response = self.client.get(reverse('education:lessons'))

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.lesson.id,
                        "link": self.lesson.link,
                        "title": self.lesson.title,
                        "description": self.lesson.description,
                        "preview": self.lesson.preview,
                        "course": self.course.id,
                        "owner": self.user.id
                    }
                ]
            }
        )

    def test_lesson_create(self):
        """Тест создания урока"""
        data = {
            'title': "test2",
            'description': 'testing2',
            'course': self.course.id,
            'owner': self.user.id,
            'link': 'https://www.youtube.com/watchargg35'
        }

        response = self.client.post(
            reverse('education:lesson_create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(Lesson.objects.all().count(), 2)

    def test_lesson_detail(self):
        """Тест вывода отдельного урока"""
        response = self.client.get(
            reverse('education:lesson_detail',
                    args=[self.lesson.id])
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                'id': self.lesson.id,
                'link': self.lesson.link,
                'title': self.lesson.title,
                'description': self.lesson.description,
                'preview': self.lesson.preview,
                'course': self.course.id,
                'owner': self.user.id
            }
        )

    def test_lesson_update(self):
        """Тест изменения урока"""
        data = {
            'name': 'test3',
            'description': 'testing3'
        }
        response = self.client.patch(
            reverse('education:lesson_update',
                    args=[self.lesson.id]),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_lesson_delete(self):
        """Тест удаления урока"""
        response = self.client.delete(
            reverse('education:lesson_delete',
                    args=[self.lesson.id])
        )

        self.assertEquals(response.status_code,
                          status.HTTP_204_NO_CONTENT)


class SubscriptionTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test11@test.ru',
            password='12qw34er',
            is_active=True
        )

        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title='test2',
            owner=self.user
        )

        self.subscription = Subscription.objects.create(
            course=self.course,
            is_active=True
        )

    def test_subscription_create(self):
        """Тест создания подписки"""
        data = {
            'user': self.user.id,
            'course': self.course.id,
            'is_active': self.subscription.is_active
        }

        response = self.client.post(
            reverse('education:subscription_create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(Subscription.objects.all().count(), 2)

    def test_subscription_delete(self):
        """Тест удаления подписки"""
        response = self.client.delete(
            reverse('education:subscription_delete',
                    args=[self.subscription.id])
        )

        self.assertEquals(response.status_code,
                          status.HTTP_204_NO_CONTENT)
