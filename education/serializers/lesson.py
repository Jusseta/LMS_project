from rest_framework import serializers
from education.models import Lesson
from education.validators import url_validator


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор модели урока"""
    link = serializers.URLField(validators=[url_validator])

    class Meta:
        model = Lesson
        fields = '__all__'
