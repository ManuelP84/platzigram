"""Post admin clases"""

# Django
from django.contrib import admin

# Models
from posts.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

