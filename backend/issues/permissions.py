from rest_framework.permissions import SAFE_METHODS, BasePermission


class CanAccessIssue(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if request.method == 'POST':
            return user.is_authenticated

        return user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.role == user.Roles.ADMIN:
            return True

        if request.method in SAFE_METHODS:
            return obj.created_by_id == user.id or obj.assigned_to_id == user.id

        if user.role == user.Roles.DEVELOPER:
            return obj.assigned_to_id == user.id

        if user.role == user.Roles.SUBMITTER:
            return request.method != 'DELETE' and obj.created_by_id == user.id

        return False
