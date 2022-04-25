from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class UserPermission(IsAuthenticated):
    """
    (IS authenticated)
    AND
    (IS superuser OR read only)
    """
    def has_object_permission(self, request, view, obj):
        print(request.user.is_superuser)
        return request.user.is_superuser or request.method in SAFE_METHODS
