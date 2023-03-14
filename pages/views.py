from django.http import HttpResponse

# Create your views here.

def homePageView(request):
    # this function is called in the pages/urls.py file when the user
    # goes to the homepage. it respondes to the request with the text "Hello World!"
    return HttpResponse ("Hello World!")
