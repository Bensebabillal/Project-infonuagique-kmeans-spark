"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

import private_storage.urls
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenVerifyView

import core.views as core
from utils.views import MyStorageView

schema_view = get_schema_view(
    openapi.Info(
        title="Chicago Crime project cloud API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@chicagocrime.ca"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # http://localhost:8000/api/admin/
    url(r'^jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('home/',core.home_view ),
    path('analysis/',core.analysis_view),
    path('data/',core.data_view ),

    path(
        'admin/password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='admin_password_reset',
    ),
    path(
        'admin/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/v1/user/', include('user.api.urls')),

    # django-user-session-URL
    url(r'', include('user_sessions.urls', 'user_sessions')),

    # Django rest auth url
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    # path('training/', include('training.urls')),
    # path('player/', include('player.urls')),
    path('api/v1/meeting/', include('django_bigbluebutton.api.urls')),
    path('api/v1/registration/', include('dj_rest_auth.registration.urls')),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    url(r'^api/v1/auth/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    url('^private-media/', include(private_storage.urls)),

    url('^private-documents/(?P<path>.*)$', MyStorageView.as_view()),

    # http://localhost:8000/
    re_path(r"^.*$", core.index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>

]
