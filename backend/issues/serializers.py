from rest_framework import serializers

from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    assigned_to_username = serializers.CharField(source='assigned_to.username', read_only=True)

    class Meta:
        model = Issue
        fields = (
            'id',
            'title',
            'description',
            'status',
            'priority',
            'created_by',
            'created_by_username',
            'assigned_to',
            'assigned_to_username',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_by', 'created_at', 'updated_at')
