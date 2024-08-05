from django.contrib.auth.models import User
from .models import Exercise, WorkoutPlan
from rest_framework import permissions, viewsets
from .permissions import IsUnAuthenticatedReadOnly, IsAdminOrReadonly
from .utils.mixin_utils import EnablePartialUpdateMixin
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ExerciseFilter, WorkOutPlanFilter
from rest_framework.decorators import action
from .viewset_actions.workout_plan_actions import (
    get_user_workout_plans,
    post_user_workout_plans,
    get_user_workout_plan,
)


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

    @action(detail=False, methods=["get", "post"], url_path="myworkoutplans")
    def my_workout_plans_actions(self, request, *args, **kwargs):

        if request.method == "POST":
            return post_user_workout_plans(request)
        elif request.method == "GET":
            return get_user_workout_plans(request)

    @action(detail=True, methods=["get"], url_path="myworkoutplans")
    def my_workout_plan_actions(self, request, *args, **kwargs):
        return get_user_workout_plan(request, **kwargs)
