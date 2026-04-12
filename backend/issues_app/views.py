from django.contrib.auth import authenticate

from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from issues.models import Issue

from .serializers import DashboardSerializer, LoginSerializer, UserSerializer


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
        )
        if user is None:
            return Response(
                {'detail': 'Invalid username or password.'},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                'token': token.key,
                'user': UserSerializer(user).data,
            }
        )


class LogoutView(APIView):
    def post(self, request):
        if hasattr(request.user, 'auth_token'):
            request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class DashboardView(APIView):
    def get(self, request):
        user = request.user
        issues = Issue.objects.all()

        if user.role == user.Roles.SUBMITTER:
            issues = issues.filter(created_by=user)
        elif user.role == user.Roles.DEVELOPER:
            issues = issues.filter(assigned_to=user)

        payload = {
            'role': user.role,
            'welcome_message': f'Welcome back, {user.username}.',
            'stats': {
                'total_issues': issues.count(),
                'open_issues': issues.filter(status=Issue.Status.OPEN).count(),
                'in_progress_issues': issues.filter(status=Issue.Status.IN_PROGRESS).count(),
                'resolved_issues': issues.filter(status=Issue.Status.RESOLVED).count(),
            },
        }

        if user.role == user.Roles.ADMIN:
            payload['summary'] = 'You can oversee users, assignments, and issue resolution.'
        elif user.role == user.Roles.DEVELOPER:
            payload['summary'] = 'You can work on assigned issues and update their status.'
        else:
            payload['summary'] = 'You can submit issues and track progress on the ones you created.'

        return Response(DashboardSerializer(payload).data)
