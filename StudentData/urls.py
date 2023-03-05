from rest_framework.routers import DefaultRouter
from django.urls import path

from StudentData.views import Student_Detail_ViewSet


router = DefaultRouter()

router.register(r'studentDetails', Student_Detail_ViewSet,
                basename='studentDetails')


urlpatterns = [
    path('student-list/', Student_Detail_ViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('student-detail/<int:pk>/', Student_Detail_ViewSet.as_view({
        'get': 'retrive',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]
