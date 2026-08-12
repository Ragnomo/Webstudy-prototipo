from django.urls import path
from . import views

urlpatterns = [
    # Rota da página inicial (Dashboard)
    path('', views.dashboard, name='dashboard'),
    
    # Rota para ver os detalhes de um curso específico
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    
    # Rota para acessar a tela dividida da aula
    path('lesson/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    
    # Rota invisível (API) que o JavaScript acessa para salvar o progresso
    path('api/complete/', views.mark_lesson_complete, name='api_complete'),
]
