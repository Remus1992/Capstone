from accounts import views
from django.urls import path
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

urlpatterns = [

    path('about/', views.about, name='about'),

    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', login, {'template_name': 'accounts/login.html'}, name="login"),
    path('logout/', logout, name="logout"),

    # Profile URLs
    path('profile/<slug:slug>/', views.profile_view, name='profile'),
    path('edit/profile/', views.profile_edit, name='edit_profile'),

    # Project URLS
    path('project/create/', views.project_create, name='project_create'),
    path('project/edit/<slug:slug>/', views.project_edit, name='project_edit'),

    # Total List of Projects
    path('project/list/', views.project_total_list, name='project_total_list'),
    path('project/view/<slug:slug>/', views.project_view, name='project_view'),

    # Message URLS
    path('send_message/', views.send_message, name='send_message'),
    path('view_received_message/', views.view_received_message, name='view_received_message'),
    path('view_single_message/<slug:slug>', views.view_single_message, name='view_single_message'),


]
