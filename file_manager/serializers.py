from rest_framework.serializers import ModelSerializer, Serializer, FileField
from rest_framework import serializers

from .models import File


class FileDataField(Serializer):
    name = serializers.CharField(read_only=True)
    size = serializers.IntegerField(read_only=True)


class FileViewSerializer(ModelSerializer):
    file = FileDataField()

    class Meta:
        model = File
        fields = ('id', 'file', 'created_at')
        read_only_fields = ['created_at']


class FileSerializer(ModelSerializer):
    file = FileField()

    class Meta:
        model = File
        fields = ('file',)
    
    def create(self, validated_data, **kwargs):
        return File.objects.create(user=kwargs['user'], **validated_data)
    
