from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("courses", viewset=views.CourseViewSet)
router.register("assignments", viewset=views.CourseAssignmentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
