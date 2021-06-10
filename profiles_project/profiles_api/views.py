from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework import viewsets
from .serializers import HelloSerializer, Hello
from .models import UserProfile
# Create your views here.


class HelloApiView(APIView):
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            "Uses HTTP methods as function (get, post, patch, put, delete)",
            "Is similar to a tradition Django View",
            "Gives you the most control over your appliction logic",
            "Is mapped manually to URLs"
        ]
        return Response({"message": "Hello!", "an_apiview": an_apiview})


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({"method": "PUT"})

    def patch(self, request):
        return Response({"method":"PATCH"})

    def delete(self, request, pk=None):
        return Response({"method":"delete"})



class HelloViewSet(viewsets.ViewSet):
    serializer_class = Hello
    def list(self, request):
        queryset = UserProfile.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = UserProfile.objects.get(pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = UserProfile.objects.get(pk=pk)
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        user = UserProfile.objects.get(pk=pk)
        user.delete()
        return Response({"deleted":"it's got deleted"})