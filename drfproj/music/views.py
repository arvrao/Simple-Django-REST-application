from django.shortcuts import render
# from music.serializers import MusicSerializer
# from rest_framework import viewsets
from music.models import Student
from django.http import Http404
# from django.db.models import Q
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class StudentAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, id):
        student = self.get_object(id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):

        student = self.get_object(id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = self.get_object(id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenericsAPIView(mixins.ListModelMixin, generics.GenericAPIView, mixins.CreateModelMixin,
    mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):

    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    lookup_field = 'id'
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    #first checks for session & then for Basic

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request, id):
        return self.create(request, id)
    
    def put(self, request, id=None):
        return self.update(request, id)
    
    def delete(self, request, id):
        return self.destroy(request, id)