from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/write/', views.make_post, name='make_post'),
    path('post/<pk>/details/', views.post_details, name='post_details'),
    path('drafts/', views.draft_posts, name='draft_posts'),
    path('post/<pk>/publish/', views.publish_post, name='publish_post'),
    path('post/<pk>/edit/', views.edit_post, name='edit_post'),
    path('post/<pk>/delete/', views.delete_post, name='delete_post'),
    path('post/done/', views.post_done_view, name='post_done')
]