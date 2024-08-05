from gym_app.admin_app.models import WorkoutPlan
from gym_app.admin_app.serializers import WorkoutPlanSerializer
from rest_framework.response import Response
from rest_framework import status


def get_user_workout_plans(request):
    """
    Handles Get Request For User Workout Plans
    """
    user = request.user
    workoutplans = WorkoutPlan.objects.filter(created_by=user)
    serializer = WorkoutPlanSerializer(workoutplans, many=True)
    return Response(serializer.data)


def get_user_workout_plan(request, **kwargs):
    """
    Return Single User Workout Plan
    """
    user = request.user
    workoutplan_id = kwargs["pk"]

    try:
        workoutplan = WorkoutPlan.objects.get(id=workoutplan_id, created_by=user)
        serializer = WorkoutPlanSerializer(workoutplan)
        return Response(serializer.data)
    except WorkoutPlan.DoesNotExist:
        return Response(
            f"Workout Plan {workoutplan_id} Does Not Exist",
            status=status.HTTP_404_NOT_FOUND,
        )


def post_user_workout_plans(request):
    """
    Handles Post Request For User Workout Plans
    """
    serializer = WorkoutPlanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
