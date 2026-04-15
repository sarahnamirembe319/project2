from rest_framework import serializers
from django.contrib.auth.models import User
from issues_app.models import Issue


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class DashboardSerializer(serializers.Serializer):
    role = serializers.CharField()
    welcome_message = serializers.CharField()
    stats = serializers.DictField()
    summary = serializers.CharField(required=False)


class IssueSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    assigned_to = UserSerializer(read_only=True)

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'status', 'priority', 
                 'created_by', 'assigned_to', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']