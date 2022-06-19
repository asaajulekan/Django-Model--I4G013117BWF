from django.db import models

# Create your models here.

from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200) 
    text=models.TextField(blank = True)
    # author=models.ForeignKey(get_user_model( ), null=True,)
    # Author=models.ForeignKey(get_user_model())
    Created_date=models.DateTimeField(default=datetime.now, blank=True )
    Published_date=models.DateTimeField(default=datetime.now, blank=True )
    # class Meta:
    #     db_table="databasee"