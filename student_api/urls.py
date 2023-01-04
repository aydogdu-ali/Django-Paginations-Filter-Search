from django.urls import path, include
from rest_framework import routers
from .views import (
    StudentMVS,
    PathMVS
)

router = routers.DefaultRouter()
router.register("student", StudentMVS)
router.register("path", PathMVS)


urlpatterns = [
   
    path("", include(router.urls))
]