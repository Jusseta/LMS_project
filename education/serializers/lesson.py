from rest_framework import serializers
from education.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор модели урока"""
    class Meta:
        model = Lesson
        fields = '__all__'
