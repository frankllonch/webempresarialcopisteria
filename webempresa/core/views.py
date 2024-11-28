from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/Historia")


def services(request):
    return render(request, "core/Servicios.html")


def store(request):
    return render(request, "core/Visítanos.html")


def contact(request):
    return render(request, "core/Contacto.html")


def blog(request):
    return render(request, "core/Blog.html")


def sample(request):
    return render(request, "core/Sample.html")
