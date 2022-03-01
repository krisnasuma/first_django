from django.urls import path

from . import views #import views dari app1

urlpatterns = [
    path('hello_world/', views.hello_world), #menambahkan path untuk browser dengan tambahan /hello_world
    path('a/', views.a),
    path('b/', views.b)
]
#membuat fungsi hello_world pada urls lalu ditampilkan ke views.py