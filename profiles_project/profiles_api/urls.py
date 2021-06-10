from django.urls import path, include
from .views import HelloApiView, HelloViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("users", HelloViewSet, basename="users")



urlpatterns = [
    path('api/', HelloApiView.as_view()),
    path("api/", include(router.urls))
]
