from django.shortcuts import render
from .models import Post



# Create your views here.
def home(request):
    content = {'posts' : Post.objects.all(),
               'title':"Smbat"}
    
    return render(request, 'home.html' , context = content)

def about(request):
    return render(request, 'about.html')