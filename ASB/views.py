from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse


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

def emailsender(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        subject = 'ASB'
        message = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail( subject, message, email_from, recipient_list )

        context = {
        'sent': 'Email successfully sent',
    }

        return JsonResponse(context, status=200)