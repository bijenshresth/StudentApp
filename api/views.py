from django.shortcuts import render
from student.models import Student
from rest_framework import generics
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

# api generic views
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student
    serializer_class = StudentSerializer


@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'Create/List': '/student/', 
        'Detail/Update/Delete': '/student/<int:pk>/',
    }

    return Response(api_urls)


# @api_view(['GET'])
# def apiOverView(request):
#     api_urls = {
#         'List': '/student-list/', 
#         'Detail View': '/student-detail/<int:pk>/',
#         'Create': '/student-create/',
#         'Update': '/student-update/<int:pk>/',
#         'Delete': '/student-delete/<int:pk>/',
#     }

#     return Response(api_urls)


# @api_view(['GET'])
# def studentList(request):
#     students = Student.objects.all()
#     serializer = StudentSerializer(students, many = True)
    
#     return Response(serializer.data)


# @api_view(['GET'])
# def studentDetail(request, pk):
#     students = Student.objects.get(id=pk)
#     serializer = StudentSerializer(students, many = False)
    
#     return Response(serializer.data)


# @api_view(['POST'])
# def studentCreate(request):
#     serializer = StudentSerializer(data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()
    
#     return Response(serializer.data)


# @api_view(['POST'])
# def studentUpdate(request, pk):
#     student = Student.objects.get(id=pk)
#     serializer = StudentSerializer(instance=student, data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()
    
#     return Response(serializer.data)


# @api_view(['DELETE'])
# def studentDelete(request, pk):
#     student = Student.objects.get(id=pk)
#     student.delete()
#     return Response('Student data successfully deleted.')