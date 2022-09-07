from django.shortcuts import render
from django.core.checks import messages
from newsletters.models import NewsletterUser
from .forms import NewsletterUserSignUpForm
from django.conf import settings

# Create your views here.
def newsletter_signup(request):
    form= NewsletterUserSignUpForm(request.POST or None)
    
    if form.is_valid():
        instance=form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'Email already exists')
        else:
            instance.save()
            messages.success(request,'Hemos enviado un correo electronico a tu correo')            
            #Correo electronico
            subject="Libro de cocina"
            from_email=settings.EMAIL_HOST_USER