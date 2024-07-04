from django.contrib.auth.models import User
from .models import Exercise, WorkoutPlan
from rest_framework import permissions, viewsets
from .permissions import IsUnAuthenticatedReadOnly
from .utils import EnablePartialUpdateMixin

from gym_app.admin_app.serializers import UserSerializer, ExerciseSerializer, WorkoutPlanSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated | IsUnAuthenticatedReadOnly]

class WorkoutPlanViewSet(EnablePartialUpdateMixin, viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated | IsUnAuthenticatedReadOnly]

    def perform_create(self, serializer):
        print(serializer)
        serializer.save(created_by=self.request.user)
