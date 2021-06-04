from django.urls import path
# to load views.py from the same dir
from . import views

app_name = "hello"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("brian", views.brian, name="brian"),
    path("david", views.david, name="david")    
]

# add hello app path in main urls.py located in the project folder. 
# in this case the project folder is lecture3
# add under urlpatterns =[ path('hello/', include("hello.urls"))] 
# and change "from django.urls import path" 
# to
# from django.urls import include, path