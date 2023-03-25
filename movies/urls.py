from django.urls import path
from . import views

# url endpoints>>movies/1/detaols -movies is a root

app_name = 'movies'
urlpatterns = [  # jango expects us to follow object map url to view function
    path('', views.index, name='index'),  # refernce>urls end point ko name kia for good practice
    path('<int:movie_id>', views.detail, name='detail')  #<define prometer>
]
