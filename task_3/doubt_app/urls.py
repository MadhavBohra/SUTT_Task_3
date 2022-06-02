from django.urls import path


#importing Views to use views functions
from . import views


# after mainapp.urls it relocates here and look for matching url patterns
# then after finding it, It calls the views.home function
urlpatterns = [
    path('',views.home, name = 'doubt-page-home'),
    path('myprofie/',views.my_profile, name = 'doubt-page-my-profile'),
    path('myquestions/',views.my_questions, name = 'doubt-page-my-questions'),
]