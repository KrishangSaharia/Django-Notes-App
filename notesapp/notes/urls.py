from django.urls import path,include
from . import views

app_name= 'notes'

urlpatterns=[
    path('<int:id>/',views.index,name="index"),
    path('<int:id>/add/', views.add, name="add"),
    path('<int:userid>/<int:noteid>/delete',views.delete, name="delete"),
    path('<int:userid>/<int:noteid>/edit', views.edit,name='edit'),
    path('<int:userid>/bin',views.bin, name='bin'),
    path('<int:userid>/<int:noteid>/bin/undo', views.undo,name='undo'),
    path('<int:userid>/<int:noteid>/bin/delete',views.bin_delete,name='bin_delete'),
]
