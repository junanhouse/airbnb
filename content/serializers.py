from rest_framework import serializers
from .models import Room, RoomType, Comment


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'

class RoomCommentSerializer(serializers.ModelSerializer):
    comment_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = Room
        fields = ['id', 'type_set', 'address',
                  'price', 'rating', 'statusStartDate',
                  'statusEndDate', 'comment_set']

class RoomTypeRoomSerializer(serializers.ModelSerializer):
    room_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = RoomType
        fields = ['name', 'image', 'room_set']
