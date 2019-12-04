from django.urls import path
from . import views
urlpatterns = [
    path("signup2/",views.register, name="signup"),
    path('login2/',views.login,name='login'),
    path('logout/',views.logout,name='logout')
]
