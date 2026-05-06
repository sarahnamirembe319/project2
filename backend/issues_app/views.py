from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import InternshipPlacement
from .serializers import InternshipPlacementSerializer


class InternshipPlacementViewSet(viewsets.ModelViewSet):
    serializer_class = InternshipPlacementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return InternshipPlacement.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)