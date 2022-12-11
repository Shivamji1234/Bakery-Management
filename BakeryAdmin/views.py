from django.http import HttpResponse

def home(request):
    print("home page")
    return HttpResponse("This is home page")