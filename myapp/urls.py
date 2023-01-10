from django.urls import path
from .views import *
 
urlpatterns = [
 
    path('', BackupView,name='backup'),
    path('restore/', RestoreView,name='restore'),
 
]
