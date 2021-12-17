from rest_framework import serializers

from django_bigbluebutton import models


class EntrainmentMeetingSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.Meeting
        fields = [
            "id",
            "author",
            "name",
            "meeting_id",
            "welcome_text",
            "created_at",
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'read_only': True},
            'author': {'read_only': True},
            'meeting_id': {'read_only': True},
            'welcome_text': {'read_only': True},
            'created_at': {'read_only': True}
        }


class JoinMeetingSerializer(serializers.Serializer):
    valid = serializers.BooleanField()
    join_link = serializers.URLField()
