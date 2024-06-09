

from django.urls import path
from django.urls import path

from . import views

from .views import CreatePostView

urlpatterns = [
   
    path('', CreatePostView.as_view(), name='add_post'),
    path('percentage/', views.index, name='index'),

]