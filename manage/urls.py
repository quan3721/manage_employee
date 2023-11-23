from django.urls import path, include
from . import views

urlpatterns = [
    path("insert/", views.add_new_employee, name='insert'),
    # path('update/', views.update_employee, name='update'),
    # path("remove/", views.remove_employee, name='remove'),
]
