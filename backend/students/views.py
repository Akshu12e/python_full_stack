from django.shortcuts import render

# Create your viw
def home (request):
    return render(request,'students/home.html')