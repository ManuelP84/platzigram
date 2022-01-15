"""
Platzigram URL Configuration

"""
# Django
from django.urls import path
from django.contrib import admin 
from django.conf import settings
from django.conf.urls.static import static
from platzigram import views as local_views
from posts import views as posts_views
from users import views as user_views


urlpatterns = [
    
    path('admin/', admin.site.urls), #admin.site.urls : Incluye todas las urls de admin
    path('hello-world', local_views.hello_world, name='hello_world'),
    path('sorted', local_views.sort_integers, name='sort'),
    path('check_age/<str:name>/<int:age>/', local_views.checking_age, name='checking_age'),

    path('', posts_views.list_posts, name='feed'),
    path('posts/new',posts_views.create_post, name='create_post'),

    path('users/login/', user_views.login_view, name='login'),
    path('users/logout/', user_views.logout_view, name='logout'),
    path('users/signup/', user_views.signup, name='signup'),
    path('users/me/profile/', user_views.update_profile, name='update_profile')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
