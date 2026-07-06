from rest_framework import serializers
from .models import *

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        read_only_fields = ['singer'] 

class SingerSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField(read_only=True)

    def get_songs(self, instance):
        serializer = SongSerializer(instance.songs, many=True)
        return serializer.data

    class Meta:
        model = Singer
        fields = ['id', 'content', 'debut', 'songs', 'created_at', 'updated_at']