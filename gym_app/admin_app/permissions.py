from rest_framework import permissions

class IsUnAuthenticatedReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow read-only access for authenticated users?  
        if request.user:
            #  Allow GET, HEAD & OPTIONS requests 
            return request.method in permissions.SAFE_METHODS
        return False