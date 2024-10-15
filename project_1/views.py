from django.http import HttpResponse
def contact(request):
    return HttpResponse("This is my email: habibbiswas350@gmail.com")

def about(request):
    return HttpResponse("Hi, this is habib")
def homepage(request):
    return HttpResponse("This Is Homepage")