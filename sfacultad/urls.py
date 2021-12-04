from os import name, path
from django.conf.urls import url, include
from django.urls import path
from .views import home, Comments, Comment_List

urlpatterns = [
    path('', home, name="Home"),
    path('comentario/', Comments, name="Coment"),
    path('list/', Comment_List, name="ListComment"),
    path('accounts/', include('django.contrib.auth.urls')),

]