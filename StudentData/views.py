from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers, viewsets, status, permissions, parsers, generics, filters
from django.http.response import HttpResponse, JsonResponse
from CollegeDetail.models import CollegeCategory, CollegeDataImage, CollegeDetailModel
from CollegeDetail.pagination import CustomPageNumberPagination

from rest_framework.pagination import PageNumberPagination

from StudentData.models import StudentDetailModel
from StudentData.serializers import Student_Detail_Serializer

# Create your views here.
class Student_Detail_ViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Students.
    """
    def list(self, request, pk=None):
        queryset = StudentDetailModel.objects.all()
        serializer_class = Student_Detail_Serializer(queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def create(self, request, pk=None):
        serializer = Student_Detail_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrive(self, request, pk=None):
        try:
            queryset = StudentDetailModel.objects.get(pk=pk)
            serializer_class = Student_Detail_Serializer(queryset)
            return JsonResponse(serializer_class.data, safe=False)
        except CollegeDetailModel.DoesNotExist:
            return Response(None, status=status.HTTP_200_OK)
        
    def partial_update(self, request, pk=None):
        try:
            queryset = StudentDetailModel.objects.get(pk=pk)
            serializer = Student_Detail_Serializer(queryset,
                                                           data=request.data,
                                                           partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except StudentDetailModel.DoesNotExist:
            return Response(None, status=status.HTTP_304_NOT_MODIFIED)

    def destroy(self, request, pk=None):
        queryset = StudentDetailModel.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)