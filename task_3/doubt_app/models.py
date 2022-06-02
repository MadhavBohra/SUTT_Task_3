from signal import default_int_handler
from django.db import models
# importing timezone to make default date as the date posted.
from django.utils import timezone
# improting User table
from django.contrib.auth.models import User

# Create your models here.
# class are like tables in database.

class Question_content(models.Model):
    topic = models.CharField(max_length=100)
    question_text = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    #models.CASCADE tells Django that if the user is delted delete all its posts.
    author = models.ForeignKey(User,on_delete=models.CASCADE)
