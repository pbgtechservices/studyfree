from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers, viewsets, status, permissions, parsers, generics, filters
from django.http.response import HttpResponse, JsonResponse
from CollegeDetail.models import CollegeCategory, CollegeDataImage, CollegeDetailModel
from CollegeDetail.pagination import CustomPageNumberPagination

from rest_framework.pagination import PageNumberPagination

from CollegeDetail.serializers import College_Detail_Serializer, College_Image_Serializer

# Create your views here.

class College_Image_ViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Images of Colleges and Results.
    """

    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def create(self, request, pk=None):
        serializer = College_Image_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = CollegeDataImage.objects.get(pk=request.data['College_Image_Id'])
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class College_Detail_ViewSet(viewsets.ViewSet):
    pagination_class = CustomPageNumberPagination
    """
    A simple ViewSet for listing or retrieving College Details.
    """

    def list(self, request, pk=None):
        try:
            
            queryset = CollegeDetailModel.objects.all().order_by('votes')
            paginator = PageNumberPagination()
            page = paginator.paginate_queryset(queryset, request)
            serializer_class = College_Detail_Serializer(page, many=True)
            return Response(serializer_class.data)
        except CollegeDetailModel.DoesNotExist:
            return Response(None, status=status.HTTP_200_OK)

    def create(self, request, pk=None):
        serializer = College_Detail_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            queryset = CollegeDetailModel.objects.get(id=serializer.data['id'])
            for img in request.data['collegeImages'] :
                queryset.collegeImages.add(img)
            for val in request.data['category'] :
                queryset.category.add(val)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrive(self, request, pk=None):
        try:
            queryset = CollegeDetailModel.objects.get(pk=pk)
            serializer_class = College_Detail_Serializer(queryset)
            return JsonResponse(serializer_class.data, safe=False)
        except CollegeDetailModel.DoesNotExist:
            return Response(None, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        try:
            queryset = CollegeDetailModel.objects.get(pk=pk)
            serializer = College_Detail_Serializer(queryset,
                                                           data=request.data,
                                                           partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                if request.data['collegeImages'] : 
                    for img in request.data['collegeImages'] :
                        queryset.collegeImages.add(img)
                if request.data['category'] :
                    for val in request.data['category'] :
                        queryset.category.add(val)
                return Response(serializer.data,
                                status=status.HTTP_202_ACCEPTED)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CollegeDetailModel.DoesNotExist:
            return Response(None, status=status.HTTP_304_NOT_MODIFIED)

    def destroy(self, request, pk=None):
        try:
            queryset = CollegeDataImage.objects.get(pk=pk)
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CollegeDetailModel.DoesNotExist:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)

class SearchCollegeDetail(viewsets.ViewSet):
    def search(self, request, key=None):
        try:
            if key == 'all' :
                categories = CollegeCategory.objects.values_list("id", flat=True)
                category_list = categories
                if request.GET.get('category'):
                    category_list = categories.filter(College_Category__icontains = request.GET.get('category'))
            else :
                category_list = CollegeCategory.objects.filter(College_Category__icontains = key)
            queryset = CollegeDetailModel.objects.filter(category__in = list(category_list.values_list('id', flat=True)))
            if request.GET.get('location'):
                    queryset = queryset.filter(location__icontains = request.GET.get('location'))
            paginator = PageNumberPagination()
            page = paginator.paginate_queryset(queryset.order_by('votes'), request)
            serializer = College_Detail_Serializer(page, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CollegeDetailModel.DoesNotExist:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)