from django.urls import path

from . import views

urlpatterns = [
    path('<int:start>/<int:end>', views.task2, name='poopy'),
    path('', views.task3),
    path('query', views.query),
    path('query/answer', views.order),

]
