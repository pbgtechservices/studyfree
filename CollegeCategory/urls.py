from rest_framework.routers import DefaultRouter
from django.urls import path

from CollegeCategory.views import College_Category_ViewSet

router = DefaultRouter()

router.register(r'collegeCategory', College_Category_ViewSet, basename='collegeCategory')

urlpatterns = [
    path('college-category-list/', College_Category_ViewSet.as_view({
            'get': 'list',
        })),
]