from django.db import models
from django.contrib.auth.models import User

class toDoList(models.Model):
    """class for listing todos"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class toDo(models.Model):
    """for managing to do"""
    list = models.ForeignKey(toDoList, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    decription = models.TextField()
    priority = models.IntegerField()
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField()
    created_data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



# Create your models here.
# TodoLists
# id: Primary key
# user: Foreign key to Users
# name: String
# created_date: DateTime
# Todos
# id: Primary key
# list: Foreign key to TodoLists
# title: String
# description: Text
# priority: Integer
# completed: Boolean
# due_date: Date
# created_date: DateTime