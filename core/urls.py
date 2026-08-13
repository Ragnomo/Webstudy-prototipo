from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    
    path('lesson/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    
    path('api/complete/', views.mark_lesson_complete, name='api_complete'),
]
