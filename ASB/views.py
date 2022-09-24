from django.shortcuts import render


def homepage(request):
    context = {}
    return render(request, 'homepage.html')

def company(request):
    context = {}
    return render(request, 'our_company.html')

def expertise(request):
    context = {}
    return render(request, 'our_expertise.html')

def projects(request):
    context = {}
    return render(request, 'our_projects.html')

def join(request):
    context = {}
    return render(request, 'join_our_team.html')

def media(request):
    context = {}
    return render(request, 'media.html')