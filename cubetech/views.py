from django.http import HttpResponse


def aboutUs(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def course(request):
    return HttpResponse("Hello, world. You're at the course index.")
