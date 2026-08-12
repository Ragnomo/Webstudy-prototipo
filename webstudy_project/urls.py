from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Rota padrão do painel de administração do Django
    path('admin/', admin.site.urls),
    
    # Inclui todas as rotas do nosso app "core" na raiz do site
    path('', include('core.urls')),
]
