from django.db import models

# Create your models here.

class Users(models.Model):
    firstname=models.CharField(max_length=15)
    lastname=models.CharField(max_length=10)
    email=models.EmailField(max_length=54, unique=True)
    username = models.CharField(max_length=20,unique=True,
        help_text=('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.firstname
