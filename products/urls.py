# This file is used to store endpoint and mappings

from django.urls import path
from . import views

# 'urlpatterns' is by convention the name given to the list that stores endpoints mapped to view functions
urlpatterns = [
    # The function views.index only gives the reference of the function, PyCharm takes care of calling that function
    path('', views.index),
    path('new', views.new)
]
