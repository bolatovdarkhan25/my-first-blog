from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.registration_view, name='register'),
    path('logout/', LogoutView.as_view(template_name='blog/post_list.html'), name='logout'),
    # path('edit_profile/<pk>/', views.profile_edit_view, name='edit_profile'),
    # path('profile_view/<int:pk>/', views.show_profile, name='show_profile'),
]
