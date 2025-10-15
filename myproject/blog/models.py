from django.db import models
from django.utils import timezone

class Client(models.Model):
    POL_CHOICES = [
        ('M', 'Male'),
        ("F", 'Female')]

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    age = models.CharField()
    pol = models.CharField(max_length=1, choices= POL_CHOICES)

    def __str__(self):
        return f"Client: {self.name} {self.surname}"

class Meet(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return f"Title: {self.title}"

class Note(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    main_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note: {self.name}"
