from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from user.models import CustomUser


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=False, max_length=255)
    last_name = serializers.CharField(required=False, max_length=255)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        }

    def save(self, request):
        user = super(CustomRegisterSerializer, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        return user


class UserSerializer(serializers.ModelSerializer):
    # player_more = serializers.SerializerMethodField()
    is_admin = serializers.SerializerMethodField()

    # document_file = serializers.ImageField(required=True)

    def get_is_admin(self, obj):
        print(obj)
        return obj.is_superuser

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'avatar', 'is_admin']

    # def get_player_more(self, instance):
    #     return instance.more
