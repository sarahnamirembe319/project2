from django.http import HttpResponse


def index(request):
    return HttpResponse('Issues app is configured correctly.')
