from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is About page")

def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("This is Contact Us page")

def service(request):
    return render(request, 'service.html')
    # return HttpResponse("This is service page")