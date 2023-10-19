from django.urls import path
from rest_framework.routers import DefaultRouter
from education.apps import EducationConfig
from education.views.course import CourseViewSet
from education.views.lesson import *
from education.views.payment import PaymentViewSet


app_name = EducationConfig.name


router_course = DefaultRouter()
router_course.register(r'course', CourseViewSet, basename='course')

router_payment = DefaultRouter()
router_payment.register(r'payment', PaymentViewSet, basename='payment')


urlpatterns = [
    path('lesson_create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/', LessonListAPIView.as_view(), name='lessons'),
    path('lesson_detail/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('lesson_update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson_delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
]

urlpatterns += router_payment.urls
urlpatterns += router_course.urls
