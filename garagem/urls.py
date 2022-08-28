from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import CategoriaViewSet, CarroViewSet, MarcaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'carro', CarroViewSet)
router.register(r'marca', MarcaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]