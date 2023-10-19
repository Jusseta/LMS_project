from rest_framework import serializers
from education.models import Course
from education.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор модели курса"""
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')

    def get_lesson_count(self, instance):
        """Вычисляет количество уроков в курсе"""
        if instance.lesson_set.all().count():
            return instance.lesson_set.all().count()
        return 0

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'lesson_count', 'lessons')
