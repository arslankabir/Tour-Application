from django.urls import path

from . import views
#   when you start the web browser this file will MAP where you wanna go
#   You can provide mutiple mapping here in urlpatterns
urlpatterns = [
    path('',views.travello, name = 'travello'),
    path('about/',views.about, name = 'about'),
    path('destinations/',views.destinations, name = 'destinations')
    ]