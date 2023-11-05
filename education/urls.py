from django.urls import path
from rest_framework.routers import DefaultRouter
from education.apps import EducationConfig
from education.views.course import CourseViewSet
from education.views.lesson import *
from education.views.payment import PaymentViewSet
from education.views.subscription import SubscriptionCreateAPIView, SubscriptionDestroyAPIView, SubscriptionListAPIView

app_name = EducationConfig.name


urlpatterns = [
    path('lesson_create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/', LessonListAPIView.as_view(), name='lessons'),
    path('lesson_detail/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('lesson_update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson_delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

    path('subscription_create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscriptions/', SubscriptionListAPIView.as_view(), name='subscriptions'),
    path('subscription_delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription_delete'),
]


router_course = DefaultRouter()
router_course.register(r'course', CourseViewSet, basename='course')

router_payment = DefaultRouter()
router_payment.register(r'payment', PaymentViewSet, basename='payment')


urlpatterns += router_payment.urls
urlpatterns += router_course.urls
