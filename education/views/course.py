from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from education.models import Course
from education.permissions import IsModerator, CoursePermission
from education.serializers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """Вьюсет для курсов"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, CoursePermission]

    def perform_create(self, serializer):
        """Добавление владельца при создании курса"""
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_queryset(self):
        """Пользователь видит только свои курсы, персонал - все"""
        queryset = super().get_queryset()
        if self.request.user.is_staff or self.request.user.is_superuser:
            queryset.all()
        else:
            queryset = queryset.filter(owner=self.request.user)

        return queryset