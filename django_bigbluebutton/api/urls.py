from django.urls import path

from . import views

urlpatterns = [
    path("meetings-list/", views.EntrainmentMeetingListAPIView.as_view()),
    path("join-meeting/", views.EntrainmentJoinMeetingAPIView.as_view()),
]
