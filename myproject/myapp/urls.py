from django.urls import path
from myapp import views

urlpatterns = [
   path('',views.index),
]

urlpatterns = [
    path('addPersonToQueue/', views.add_person_to_queue, name='add_person_to_queue'),
    # เพิ่มเส้นทางอื่นๆ ตามต้องการ
]


