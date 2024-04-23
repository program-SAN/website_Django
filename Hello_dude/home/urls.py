from django.contrib import admin
from django.urls import path
from home import views

#did manually for admin page
admin.site.site_header = "NATURE Admin"
admin.site.site_title = "SANJAY NATURE Admin Portal"
admin.site.index_title = "Welcome to NATURE"

urlpatterns = [
    path('', views.index,name='home'),
    path('about', views.about,name='about'),
    path('services', views.services,name='services'),
    path('contact', views.contact,name='contact'),

]