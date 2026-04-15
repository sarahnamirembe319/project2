from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import Issue
from .permissions import CanAccessIssue
from .serializers import IssueSerializer


class IssueViewSet(viewsets.ModelViewSet):

    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated, CanAccessIssue]

    def get_queryset(self):

        user = self.request.user
        queryset = Issue.objects.select_related('created_by', 'assigned_to')

        if user.role == user.Roles.ADMIN:
            return queryset

        if user.role == user.Roles.DEVELOPER:
            return queryset.filter(assigned_to=user)

        return queryset.filter(created_by=user)


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)