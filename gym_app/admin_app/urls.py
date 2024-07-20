from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"exercises", views.ExerciseViewSet, basename="exercise")
router.register(r"workoutplans", views.WorkoutPlanViewSet, basename="workoutplan")


urlpatterns = [
    path("", include(router.urls)),
]
