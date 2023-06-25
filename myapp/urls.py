from django.urls import path
from .views import home, view_name, view_name_bombastic, view_name_ram, json_view, index, student, page1, page2, student_detail

urlpatterns = [
    path('name/ram/', view_name_ram),
    path('name/mr.bombastic/', view_name_bombastic),
    path('get-name/<str:name>/', view_name),
    path('json-view/', json_view),
    path('', home),
    path('index/', index),
    path('students/', student, name="students"),
    path('student/<int:id>/', student_detail, name="student_detail"),
    path('page1/', page1),
    path('page2/', page2)
]
