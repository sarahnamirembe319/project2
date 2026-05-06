from rest_framework import generics
from .models import InternshipPlacement
from .serializers import IssueSerializer


class InternshipPlacementListCreateView(generics.ListCreateAPIView):
    queryset = InternshipPlacement.objects.all()
    serializer_class = IssueSerializer


class InternshipPlacementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InternshipPlacement.objects.all()
    serializer_class = IssueSerializer