from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from issues.models import Issue

User = get_user_model()


class AuthenticationTests(APITestCase):
    def setUp(self):
        self.password = 'StrongPass123!'
        self.user = User.objects.create_user(
            username='submitter1',
            password=self.password,
            role=User.Roles.SUBMITTER,
        )

    def test_login_returns_token_and_user_role(self):
        response = self.client.post(
            reverse('login'),
            {'username': self.user.username, 'password': self.password},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertEqual(response.data['user']['role'], User.Roles.SUBMITTER)


class DashboardTests(APITestCase):
    def setUp(self):
        self.password = 'StrongPass123!'
        self.developer = User.objects.create_user(
            username='dev1',
            password=self.password,
            role=User.Roles.DEVELOPER,
        )
        self.submitter = User.objects.create_user(
            username='submitter1',
            password=self.password,
            role=User.Roles.SUBMITTER,
        )
        self.other_submitter = User.objects.create_user(
            username='submitter2',
            password=self.password,
            role=User.Roles.SUBMITTER,
        )
        Issue.objects.create(
            title='Assigned issue',
            description='Needs work',
            created_by=self.submitter,
            assigned_to=self.developer,
        )
        Issue.objects.create(
            title='Someone else issue',
            description='Not assigned to dev',
            created_by=self.other_submitter,
        )

    def test_developer_dashboard_only_counts_assigned_issues(self):
        token = Token.objects.create(user=self.developer)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

        response = self.client.get(reverse('dashboard'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['stats']['total_issues'], 1)
