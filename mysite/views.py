from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello, world! This is a simple Django single-page site.</h1>')
