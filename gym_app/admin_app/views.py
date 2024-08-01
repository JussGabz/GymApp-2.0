from django.contrib.auth.models import User
from .models import Exercise, WorkoutPlan
from rest_framework import permissions, viewsets
from .permissions import IsUnAuthenticatedReadOnly, IsAdminOrReadonly
from .utils.mixin_utils import EnablePartialUpdateMixin
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ExerciseFilter, WorkOutPlanFilter
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.decorators import action
from rest_framework.response import Response


from gym_app.admin_app.serializers import (
    UserSerializer,
    ExerciseSerializer,
    WorkoutPlanSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExerciseViewSet(viewsets.ModelViewSet):

    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ExerciseFilter
    permission_classes = [IsAdminOrReadonly]


class WorkoutPlanViewSet(EnablePartialUpdateMixin, viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = WorkOutPlanFilter
    permission_classes = [permissions.IsAuthenticated | IsUnAuthenticatedReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    @action(detail=False, methods=['get'], url_path="myworkoutplans")
    def get_my_workouts(self, request):
        user = request.user
        workouts = WorkoutPlan.objects.filter(created_by=user)
        serializer = self.get_serializer(workouts, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'], url_path='myworkoutplans')
    def get_my_workout_plan_by_id(self, request, pk):
        workout_plan = WorkoutPlan.objects.get(id=pk)
        serializer = self.get_serializer(workout_plan)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'], url_path='myworkoutplans')
