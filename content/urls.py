from django.urls import path
from django.conf.urls import include
from .views import RoomViewset, RoomTypeViewset, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('room', RoomViewset)
router.register('roomtype', RoomTypeViewset)
router.register('comment', CommentViewSet)
urlpatterns = [
    path('', include(router.urls))
]