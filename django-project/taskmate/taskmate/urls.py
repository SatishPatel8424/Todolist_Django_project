from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolist_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  todolist_view.index, name='index'),
    path('todolist/', include('todolist_app.urls')),
    path('contact-us',  todolist_view.contact, name='contact'),
    path('about-us', todolist_view.about, name='about'),
   
]
