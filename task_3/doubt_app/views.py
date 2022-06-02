from django.shortcuts import render
from django.http import HttpResponse


from .models import Question_content



# Create your views here.
# Logic to Handel what happens when you are redirected to some route

# Instead of writing whole html code for each respone we use templates
#by default django looks for a templeates directory in each of our app

#Add the app to list of installed app in setting.py so django looks for a templates directory

#Shortcut to display html templates from templates folder is using shortcut Render

# Manual Data Entry
# question_content = [
#     {'name' : 'Madhav Bohra',
#     'id' : '2021A2PS2155P',
#     'date' : '01 Jun 2022',
#     'topic' : 'Array',
#     'question_text' : 'Write a program to cyclically rotate an array by one'}
    
# ]


def home(request):

    context = {
        'question_content' : Question_content.objects.all()
    }
    #Displaying html templates
    #render function takes 3 input
    # request, location of template and context (way to pass information to our templates)
    # we can write code in our html templates, as pyton use jinja engine to decode it
    # Templating engine is similar to jinja 2
    # we can pass .json file as a context

    return render(request, 'doubt_app/home.html',context)

def my_profile(request):
     return render(request, 'doubt_app/myprofile.html')

def my_questions(request):
     return render(request, 'doubt_app/myquestions.html')