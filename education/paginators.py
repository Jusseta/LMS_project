from rest_framework.pagination import PageNumberPagination


class CoursePaginator(PageNumberPagination):
    """Пагинатор для курсов"""
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 20


class LessonPaginator(PageNumberPagination):
    """Пагинатор для уроков"""
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 20
