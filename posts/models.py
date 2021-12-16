"""Post models."""

# Django
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='posts/pictures')

    created = models.DateField(auto_now_add=True) # auto_now_add: time and date of creation of record.
    modified = models.DateField(auto_now=True)

    def __str__(self):
        """Return title and username"""

        return f'{self.title} by @{self.user.username}'
























# """Posts models."""

# # Django
# from django.db import models

# class User(models.Model):
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=20)

#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)

#     is_admin = models.BooleanField(default=False)

#     bio = models.TextField(blank=True)

#     birthdate = models.DateField(blank=True, null=True)
    
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         """Returns the email."""
        
#         return self.email
