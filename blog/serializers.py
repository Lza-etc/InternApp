from rest_framework import serializers
from blog.models import Users
from django.core.exceptions import ValidationError


def name_length(value):
    if len(value)<2:
        raise serializers.ValidationError("Name is too short")

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    firstname=serializers.CharField(validators=[name_length])
    lastname=serializers.CharField()
    email=serializers.EmailField()
    username = serializers.CharField()
    active=serializers.BooleanField(default=True)

    def validate_username(self,value):
        if len(value) <2:
            raise serializers.ValidationError("UserName is too short!")
        else:
            return value




