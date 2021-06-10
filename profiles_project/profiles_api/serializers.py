from rest_framework import serializers
from .models import UserProfile


class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)

class Hello(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"