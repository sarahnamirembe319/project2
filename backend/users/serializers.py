from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'role')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(trim_whitespace=False)


class DashboardStatsSerializer(serializers.Serializer):
    total_issues = serializers.IntegerField()
    open_issues = serializers.IntegerField()
    in_progress_issues = serializers.IntegerField()
    resolved_issues = serializers.IntegerField()


class DashboardSerializer(serializers.Serializer):
    role = serializers.CharField()
    welcome_message = serializers.CharField()
    summary = serializers.CharField()
    stats = DashboardStatsSerializer()
