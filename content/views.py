from .models import Room, RoomType, Comment
from .serializers import RoomSerializer, RoomTypeSerializer, CommentSerializer, RoomCommentSerializer, RoomTypeRoomSerializer
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import action
from django.db.models import Count, Avg


class RoomViewset(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    detail_serializer_class = RoomCommentSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['rating', 'type_set']
    ordering = ['-rating']

    def get_serializer_class(self):
         if self.action == 'retrieve':
             return self.detail_serializer_class
         return super().get_serializer_class()

class RoomTypeViewset(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    detail_serializer_class = RoomTypeRoomSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
