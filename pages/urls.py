from django.urls import path
from .views import homePageView

urlpatterns = [
    # user is routed here from the django_project/urls.py, now homePageView is 
    # is called, which returns the HttpResponse "Hello World!"
    path("", homePageView, name="home"),
]