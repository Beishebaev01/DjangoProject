from django.shortcuts import render, HttpResponse


def test_view(request):
    return HttpResponse("Hello, world!")


def html_view(request):
    return render(request, 'base.html')