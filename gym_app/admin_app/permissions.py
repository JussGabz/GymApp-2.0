from rest_framework import permissions


class IsUnAuthenticatedReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow read-only access for authenticated users?
        if request.user:
            #  Allow GET, HEAD & OPTIONS requests
            return request.method in permissions.SAFE_METHODS
        return False


class CanReadExercisesOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("admin_app.view_exercises")


class ReadOnlyPermission(permissions.BasePermission):
    """
    Custom Permission for read-only Access
    """

    def has_permission(self, request, view):
        # CHeck if the request method is in SAFE_METHODS (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return request.user.has_perm("admin_app.readonly_exercises")
        return False


class IsAdminOrReadonly(permissions.BasePermission):
    """
    Custom permission to grant read-only access for non-admins and full access for admins.
    """

    def has_permission(self, request, view):
        # Allow read-only (safe) methods for all users
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated

        # Allow non-safe methods (POST, PUT, DELETE) only for admin users
        return request.user and request.user.is_staff
