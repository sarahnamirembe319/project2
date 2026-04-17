from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.profile.role == "admin"


class CanAccessIssue(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.profile.role == "admin":
            return True
        if request.user.profile.role == "developer":
            return obj.assigned_to == request.user
        return obj.created_by == request.user