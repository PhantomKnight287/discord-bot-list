from django.urls import path
from . import views
from django.contrib import admin
admin.site.site_title = "Discord Bot List Admin"
admin.site.index_title = "Discord Bot List Admin"
admin.site.site_header = "Discord Bot List Admin"
urlpatterns = [
    path('', views.index, name='home'),
    path('submit', views.submitBot, name="submit")
]
