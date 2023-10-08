from django.shortcuts import render
from .models import *


def index(request):
    home = Home.objects.latest("updated")
    about = About.objects.latest('updated')
    skills = Skills.objects.all()

    context = {"home": home,
                "about": about,
            'skills': skills
            }

    return render(request, "index.html", context)


# Create your views here.
