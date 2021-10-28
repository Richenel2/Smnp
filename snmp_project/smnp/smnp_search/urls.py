from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'categorie', CategorieViewSet)
router.register(r'equipement', EquipementViewSet)
router.register(r'use', UseViewSet)
router.register(r'down', DownViewSet)
router.register(r'interface', InterfaceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("start/",start),
    path("stop/",stop),
]