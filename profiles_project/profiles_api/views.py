from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .serializers import HelloSerializer
# Create your views here.


class HelloApiView(APIView):
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            "Uses HTTP methods as function (get, post, patch, put , delete)",
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