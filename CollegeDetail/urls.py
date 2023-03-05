from rest_framework.routers import DefaultRouter
from django.urls import path

from CollegeDetail.views import College_Detail_ViewSet, College_Image_ViewSet, SearchCollegeDetail


router = DefaultRouter()

router.register(r'collegeDetails', College_Detail_ViewSet, basename='collegedetails')
router.register(r'collegeImages', College_Image_ViewSet, basename='collegeImages')
router.register(r'searchcollege', SearchCollegeDetail, basename='collegeImages')

urlpatterns = [
    path('college-image-list/', College_Image_ViewSet.as_view({
            'post': 'create',
            'delete': 'destroy'
        })),
    path('college-list/', College_Detail_ViewSet.as_view({
            'get': 'list',
            'post': 'create'
        })),
    path('college-detail/<int:pk>/', College_Detail_ViewSet.as_view({
            'get': 'retrive',
            'patch' : 'partial_update'
        })),
    path('search-college-detail/<str:key>/', SearchCollegeDetail.as_view({
            'get': 'search',
            # 'post': 'create'
        }))
]