from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def course_details(request):
    return render(request, 'course_details.html')

def courses(request):
    return render(request, 'courses.html')

def events(request):
    return render(request, 'events.html')

def pricing(request):
    return render(request, 'pricing.html')

def trainers(request):
    return render(request, 'trainers.html')

def starter_page(request):
    return render(request, 'starter-page.html')

def show(request):
    return render(request, 'show.html')