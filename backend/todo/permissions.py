from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class ProjectPermission(IsAuthenticated):
    """
    (IS authenticated)
    AND
    (IS superuser OR project owner OR project contributor read only)
    """
    def has_object_permission(self, request, view, obj):
        possible_users = list(obj.users.values_list('user', flat=True))
        possible_users.append(obj.created_by.id)
        if request.user.id not in possible_users and not request.user.is_superuser:
            return False
        return request.user.is_superuser or obj.created_by == request.user or request.method in SAFE_METHODS


class TaskPermission(IsAuthenticated):
    """
    (IS authenticated)
    AND
    (IS superuser OR task project owner OR task contributor)
    """
    def has_object_permission(self, request, view, obj):
        possible_users = list(obj.project.users.values_list('user', flat=True))
        possible_users.append(obj.project.created_by.id)
        return request.user.is_superuser or request.user.id in possible_users
