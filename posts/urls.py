from django.contrib import admin
from django.urls import path
from posts import views
urlpatterns=[
    path('',views.home_view,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('post/<int:id>/',views.post_delete,name='post_delete'),  
    path('trash/',views.trash_view,name='trash_view'),
    path('restore/<int:id>/',views.restore_post,name='restore_post'),
    path('permanent_delete/<int:id>/',views.permanent_delete,name='permanent_delete'),
    path('post_detail/<int:id>/',views.post_detail,name='post_detail'),
    
]