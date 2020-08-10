from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def home(request):
    users_p = get_object_or_404(Userp)
    socials = Social.objects.all()
    education = Education.objects.all()
    exprience = Experience.objects.all()
    skills = Skill.objects.all()
    context = {
        'usersd' : users_p,
        'socials' : socials,
        'education' : education,
        'exprience' : exprience,
        'skill' : skills
    }
    return render(request, 'index.html', context)

