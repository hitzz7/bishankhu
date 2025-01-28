from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Bishankhu/home.html')

def product(request):
    return render(request,'Bishankhu/product.html')
def service(request):
    return render(request,'Bishankhu/service.html')
def about(request):
    return render(request,'Bishankhu/about.html')
def contact(request):
    return render(request,'Bishankhu/contact.html')
def message(request):
    return render(request,'Bishankhu/message.html')