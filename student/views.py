from django.shortcuts import render
from  rest_framework.views import APIView
from .models import StudentProfile,User
from .serializer import StudentProfileSerializer,UserSerializer
from rest_framework.response import Response
# Create your views here.

class UserListView(APIView):
    def get(self, request):
        udata = User.objects.all()
        serializer = UserSerializer(udata,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
class UserProfileView(APIView):
    def put(self,request,pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    def patch(self,request,pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    def delete(self,request,pk):
        user=User.objects.get(pk=pk)
        user.delete()
        return Response(status=204)
class StudentCreateRetriveView(APIView):
    def get(self, request):
        studata = StudentProfile.objects.all()
        serializer = StudentProfileSerializer(studata,many=True)
        return Response(serializer.data)
    
    def post(self, request):
     
        serializer = StudentProfileSerializer(data=request.data)
        
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class StudentProfileView(APIView):      
    def put(self, request, pk):
        student = StudentProfile.objects.get(pk=pk)
        serializer = StudentProfileSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def patch(self, request, pk):
        student = StudentProfile.objects.get(pk=pk)
        serializer = StudentProfileSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        student = StudentProfile.objects.get(pk=pk)
        student.delete()
        return Response(status=204)