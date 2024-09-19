from gym_app.admin_app.models import WorkoutPlan
from gym_app.admin_app.serializers import WorkoutPlanSerializer
from gym_app.admin_app.filters import WorkOutPlanFilter
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


def get_user_workout_plans(request):
    """
    Handles Get Request For User Workout Plans
    """
    user = request.user
    workoutplans = WorkoutPlan.objects.filter(created_by=user)

    # Grab FilterSet Class
    filterset = WorkOutPlanFilter(request.GET, queryset=workoutplans)

    # If Filterset is not valid, return error
    if not filterset.is_valid():
        return Response(filterset.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = WorkoutPlanSerializer(filterset.qs, many=True)
    return Response(serializer.data)


def get_user_workout_plan(request, **kwargs):
    """
    Return Single User Workout Plan
    """
    user = request.user
    workoutplan_id = kwargs["pk"]
    workoutplan = get_object_or_404(WorkoutPlan, pk=workoutplan_id, created_by=user)
    serializer = WorkoutPlanSerializer(workoutplan)
    return Response(serializer.data)


def post_user_workout_plans(request):
    """
    Handles Post Request For User Workout Plans
    """
    serializer = WorkoutPlanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
