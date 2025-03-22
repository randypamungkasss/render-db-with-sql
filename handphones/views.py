from django.shortcuts import render
from .models import Handphone 

# Create your views here.
def index_view(request):

    handphones = Handphone.objects.all() 

    context = {
        "handphones":handphones
    }

    return render(request, "index.html", context)
