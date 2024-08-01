import pytest
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from gym_app.admin_app.models import Exercise


@pytest.mark.django_db()
def test_user_exercise_perm():
    # Create a User
    test_user = User.objects.create_user("Test_User", "test@jussgym.com", "testuser")

    content_type = ContentType.objects.get_for_model(Exercise)
    permission = Permission.objects.get(
        codename='view_exercises',
        content_type=content_type,
    )

    # Assign the permission to the user
    test_user.user_permissions.add(permission)
    test_user.save()

    print(test_user.get_all_permissions())



    # # Test Permissions
    # assert test_user.has_perm('gym_app.add_exercise') is True
    # assert test_user.has_perm('gym_app.change_exercise') is True
    # assert test_user.has_perm('gym_app.delete_exercise') is True
    assert test_user.has_perm('admin_app.view_exercises') is True

    # Create Permission To CRUD Exercises
    # Create Permission To CRUD Workout Plans
