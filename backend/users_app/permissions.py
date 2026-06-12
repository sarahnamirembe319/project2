from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.profile.role == "admin"


class CanAccessInternshipPlacement(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.profile.role == "admin":
            return True
        if request.user.profile.role == "developer":
            return obj.assigned_to == request.user
        return obj.created_by == request.user 

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'

class IsWorkplaceSupervisor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'workplace_supervisor'

class IsAcademicSupervisor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'academic_supervisor'

class IsInternshipAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class IsAdminOrAcademicSupervisor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['admin', 'academic_supervisor']

class IsSupervisor(BasePermission):
    """Allows both workplace and academic supervisors."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [
            'workplace_supervisor', 'academic_supervisor'
        ] 