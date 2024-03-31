from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from . forms import userForm


def Home(request):
    c = ''
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == "+":
                c = n1 + n2
            elif opr == " - ":
                c = n1 - n2
            elif opr == "*":
                c = n1 * n2
            elif opr == "/":
                c = n1 / n2

    except:
        c = "Invalid Operations"
    print(c)
    return render(request, "home.html", {'c': c})


def About(request):
    if request.method == 'GET':
        output = request.GET.get('output')
        context = {
            'output': output
        }
    return render(request, "about.html", context)


def Contact(request):
    #   Case 1
    #  try:
    #     n1 = int(request.GET['num1'])
    #     n2 = int(request.GET['num2'])
    #     print(n1+n2)
    # except:
    #     pass

    # #   Case 2
    # finalAns = 0
    # try:
    #     if request.method == 'GET':
    #         n1 = int(request.GET.get('num1'))
    #         n2 = int(request.GET.get('num2'))
    #         finalAns = n1+n2
    #         print(n1+n2)
    # except:
    #     pass

    #   Case 2
    finalAns = 0
    fn = userForm()
    context = {'form': fn, }
    try:
        if request.method == 'POST':
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalAns = n1+n2
            print(n1+n2)

            context = {
                'n1': n1,
                'n2': n2,
                'output': finalAns,
                'form': fn,
            }
            url = "/about/?output={}".format(finalAns)
            # return HttpResponseRedirect(url)
            # or
            return redirect(url)
    except:
        return HttpResponse(url)
    return render(request, "contact.html", context)


def Service(request):
    return render(request, "service.html")


def Blog(request):
    return render(request, "blog.html")


def Submitform(request):
    try:
        if request.method == 'POST':
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalAns = n1+n2
            print(n1+n2)

            context = {
                'n1': n1,
                'n2': n2,
                'output': finalAns
            }
            url = "/about/?output={}".format(finalAns)
            # return HttpResponseRedirect(url)
            # or
            return redirect(url)
    except:
        pass


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
