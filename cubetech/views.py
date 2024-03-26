from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    context = {
        'title': 'Sirah Tech',
        'welcome': 'Welcome to Sirah Tech | Kashmir',
        'clist': ['html', 'css', 'js', 'react'],
        'number': [10, 20, 30, 40, 50, 60, 70, 80, 90,],
        'std_detail': [
            {'name': 'Admin', 'id': 12345},
            {'name': 'User', 'id': 67890},
        ]
    }
    return render(request, "index.html", context)


def aboutUs(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def course(request):
    return HttpResponse("Hello, world. You're at the course index.")


def courseDetail(request, courseid):
    return HttpResponse(courseid)


def courseDetails(request, coursestr):
    return HttpResponse(coursestr)
