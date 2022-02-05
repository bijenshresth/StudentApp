from django.urls import path
from . import views


urlpatterns = [
    # api path
    path('students', views.StudentList.as_view()),
    path('student/<int:pk>', views.StudentDetail.as_view()),
    path('', views.apiOverView, name='api-overview'),

    # path('student-list', views.studentList, name='student-list'),
    # path('student-detail/<int:pk>/', views.studentDetail, name='student-detail'),
    # path('student-create/', views.studentCreate, name='student-create'),
    # path('student-update/<int:pk>', views.studentUpdate, name='student-update'),
    # path('student-delete/<int:pk>', views.studentDelete, name='student-delete'),
]
   