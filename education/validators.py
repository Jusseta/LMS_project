from rest_framework.serializers import ValidationError


ALLOWED_URL = 'https://www.youtube.com/'


def url_validator(value):
    """Валидатор ссылок"""
    if ALLOWED_URL not in value.lower():
        raise ValidationError('Допускается ссылка только на YouTube')
