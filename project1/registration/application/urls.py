from django.urls import path
from . import views

urlpatterns=[
    path('',views.fun,name='home'),
    path('register/',views.register,name='register'),
    path('signin/',views.signin,name='signin'),
    path('task/',views.task,name='task'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('finished/<int:id>',views.finished,name='finished')
]