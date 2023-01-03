from . import views 
from django.urls import path
urlpatterns=[
path('list/',views.studentList),
path('add/',views.AddStu),
path('update/',views.update),
path('delete/',views.deleteStu),
]