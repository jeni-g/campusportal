from django.db import models
from django.contrib.auth.models import User

class EventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    register_number = models.CharField(max_length=15)
    phone = models.CharField(max_length=10)
    event = models.CharField(max_length=50)
    submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student_name + "-" + self.event
    
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    email = models.EmailField()
    batch_year = models.IntegerField()
    department = models.CharField(max_length=100)
    message_type = models.CharField(max_length=20,) 
    message = models.TextField()
    status = models.CharField(max_length=20, default='pending')
    submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name + " - " + self.message_type
# Create your models here.
