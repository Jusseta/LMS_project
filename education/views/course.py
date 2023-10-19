from rest_framework import viewsets

from education.models import Course
from education.serializers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """Вьюсет для курсов"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
