from django.urls import path
from myapp import views
from . import views

urlpatterns = [
    path('', views.simulate_bakery_queue, name='simulate_bakery_queue'),
]

#urlpatterns = [
#   path('',views.index),
#    path('about',views.about),
#    path('form',views.form)
#]


