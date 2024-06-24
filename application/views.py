from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignupForm
import math, random
from django.contrib import messages
from .models import Registration 
from django.core.mail import send_mail
from django.conf import settings

import logging
logger = logging.getLogger(__name__)
print(logger)

# Create your views here.

def home(request):
    logger.info('Hello Manish What are you doing today !')

    return HttpResponse("welcome to my home page")


def signup(request):
    if request.method == 'POST':
        logger.info('Hello Manish What are you doing today !')
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            subject = '<h1>This Email For Register<h1>'
            message = f'this is you email'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]
            try:
                send_mail(subject, message, from_email, recipient_list)
                logger.info("Mail Send Successfukkky")
                return redirect('home')
            except Exception as e:
                return HttpResponse(f'Error sending email: {e}')
    else:
        form = SignupForm()
        print("llllllllllllllllllllllllllllllllll")
    return render(request, 'signup.html', {'form': form})





