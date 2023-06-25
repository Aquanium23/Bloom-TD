from django.urls import path
from .views import home, classroom, add_student, detail_student, student_update, classroom_delete, student_delete

urlpatterns = [
    path('student-delete/<int:id>/', student_delete, name='crud_student_delete'),
    path('classroom-delete/<int:id>/', classroom_delete, name='classroom_delete'),
    path('add-student/', add_student, name='add_student'),
    path('detail-student/<int:id>/', detail_student, name='detail_student'),
    path("classroom/", classroom, name="crud_classroom"),
    path('student-update/<int:id>/', student_update, name='student_update'),
    path('', home, name='crud_home')
]
