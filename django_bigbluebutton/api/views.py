from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from django_bigbluebutton import models
from django_bigbluebutton.api.serializers import JoinMeetingSerializer
from django_bigbluebutton.bbb import BigBlueButton
from django_bigbluebutton.models import Meeting
from . import serializers


class EntrainmentMeetingListAPIView(viewsets.generics.ListAPIView):
    """ViewSet for the EntrainmentPhase class"""

    queryset = models.Meeting.objects.filter(is_running=True)
    serializer_class = serializers.EntrainmentMeetingSerializer
    permission_classes = [permissions.IsAuthenticated]


class EntrainmentJoinMeetingAPIView(APIView):

    def get(self, request):
        # print('hello' + request.GET.get('meeting_id', None))

        try:
            meeting = Meeting.objects.get(pk=request.GET.get('meeting_id', 1), is_running=True)
        except Meeting.DoesNotExist:
            meeting = None

        if meeting is None:
            serializer = JoinMeetingSerializer({"valid": False, "join_link": ""}, context={'request': request})
            return Response(serializer.data)

        link = BigBlueButton().join_url(meeting.meeting_id, request.user.username, meeting.attendee_password)
        serializer = JoinMeetingSerializer({"valid": True, "join_link": link}, context={'request': request})
        return Response(serializer.data)
