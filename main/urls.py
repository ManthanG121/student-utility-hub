from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="Home"),
    path('/about',views.about,name="About"),
    path('/contact',views.contact,name="Contact"),
    path('/student',views.student,name="Student"),
    path('/mark',views.mark,name='Mark'),
    path('/gallery',views.gallery,name="Gallery"),
]
