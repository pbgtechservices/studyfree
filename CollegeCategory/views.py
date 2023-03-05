from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers, viewsets, status, permissions, parsers, generics, filters
from django.http.response import HttpResponse, JsonResponse

from CollegeCategory.models import CollegeCategoryModel
from CollegeCategory.serializers import College_Category_Serializer

# Create your views here.

class College_Category_ViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Images of Colleges and Results.
    """

    def list(self, request):
        queryset = CollegeCategoryModel.objects.all()
        serializer = College_Category_Serializer(queryset, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)