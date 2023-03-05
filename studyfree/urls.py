"""studyfree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls.conf import include
from django.conf import settings  # new
from django.conf.urls.static import static  # new
from allauth.account.views import ConfirmEmailView,  PasswordResetView
from allauth.account.views import confirm_email as allauthemailconfirmation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    url('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetView.as_view(),
         name='account_reset_password_from_key'),
    # url('password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', TemplateView.as_view(),  name='password_reset_confirm'),
    path('api/v1/rest-auth/registration/',  # new
         include('rest_auth.registration.urls')),
    path('api-auth/api/v1/rest-auth/registration/verify-email/<str:key>/', ConfirmEmailView.as_view(),
         name='account_confirm_email'),
     # MyApps Urls
    path('college/', include('CollegeDetail.urls')),
    # path('category/', include('CollegeCategory.urls')),
]
