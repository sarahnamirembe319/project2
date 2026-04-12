from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Issue

User = get_user_model()


class IssuePermissionTests(APITestCase):
    def setUp(self):
        self.password = 'StrongPass123!'
        self.admin = User.objects.create_user(
            username='admin1',
            password=self.password,
            role=User.Roles.ADMIN,
        )
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
        self.issue = Issue.objects.create(
            title='Broken login',
            description='Users cannot sign in',
            created_by=self.submitter,
            assigned_to=self.developer,
        )

    def authenticate(self, user):
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

    def test_submitter_only_sees_own_issues(self):
        self.authenticate(self.submitter)

        response = self.client.get('/api/issues/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_other_submitter_cannot_access_issue_detail(self):
        self.authenticate(self.other_submitter)

        response = self.client.get(f'/api/issues/{self.issue.id}/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_developer_can_update_assigned_issue(self):
        self.authenticate(self.developer)

        response = self.client.patch(
            f'/api/issues/{self.issue.id}/',
            {'status': Issue.Status.IN_PROGRESS},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], Issue.Status.IN_PROGRESS)
