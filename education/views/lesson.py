from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from education.models import Lesson
from education.paginators import LessonPaginator
from education.permissions import IsModerator, IsOwner
from education.serializers.lesson import LessonSerializer
from education.tasks import send_update_course_message


class LessonCreateAPIView(generics.CreateAPIView):
    """Создание урока"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        """Добавление владельца при создании урока и отправка сообщения об обновлении"""
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()

        send_update_course_message.delay(new_lesson.course.id)


class LessonListAPIView(generics.ListAPIView):
    """Список уроков"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = LessonPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Пользователь видит только свои курсы, персонал - все"""
        queryset = super().get_queryset()
        if self.request.user.is_staff or self.request.user.is_superuser:
            queryset.all()
        else:
            queryset = queryset.filter(owner=self.request.user.id)

        return queryset


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Страница с деталями урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Изменение урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]

    def perform_update(self, serializer):
        """Добавление владельца при создании урока и отправка сообщения об обновлении"""
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()

        send_update_course_message.delay(new_lesson.course.id)


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Удаление урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
