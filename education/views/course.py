from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from education.models import Course
from education.paginators import CoursePaginator
from education.permissions import CoursePermission
from education.serializers.course import CourseSerializer
from education.tasks import send_update_course_message


class CourseViewSet(viewsets.ModelViewSet):
    """Вьюсет для курсов"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator
    permission_classes = [IsAuthenticated, CoursePermission]

    def perform_create(self, serializer):
        """Добавление владельца при создании курса"""
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def perform_update(self, serializer):
        upd_course = serializer.save()
        if upd_course:
            send_update_course_message.delay(upd_course.id)

    def get_queryset(self):
        """Пользователь видит только свои курсы, персонал - все"""
        queryset = super().get_queryset()
        if self.request.user.is_staff or self.request.user.is_superuser:
            queryset.all()
        else:
            queryset = queryset.filter(owner=self.request.user)

        return queryset
