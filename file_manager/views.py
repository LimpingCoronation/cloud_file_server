from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.authtoken.models import Token
from django.http import FileResponse
from django.conf import settings
import os

from .mixins import Protected
from .serializers import FileSerializer, FileViewSerializer
from .models import File


def get_token_from_request(request):
    token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
    user = Token.objects.get(key=token).user

    return user


def does_user_has_file(user, pk):
    file = File.objects.filter(id=pk)

    if not file.exists():
        return Response({
            'detail': 'Нет такого файла',
        }, status=404)
    
    file = file.first()

    if not file.user == user:
        return Response({
            'detail': 'У вас нет доступа к этому файлу',
        }, status=404)
    
    return file


class GetFileListView(Protected, ListAPIView):

    serializer_class = FileViewSerializer
    
    def get_queryset(self):
        user = get_token_from_request(self.request)

        return File.objects.filter(user=user)


class UploadFileView(Protected, APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        user = get_token_from_request(self.request)

        serializer = FileSerializer(
            data=request.data
        )

        if not serializer.is_valid():
            print(serializer.error_messages)
            return Response({
                "detail": "Не валидные данные"
            }, status=400)
        
        serializer.create(validated_data=serializer.validated_data, user=user)
        return Response({
            'message': 'ok',
        }, 204)
        

class DeleteFileView(Protected, APIView):
    def delete(self, request, pk):
        user = get_token_from_request(request)

        file = does_user_has_file(user, pk)

        if type(file) == Response:
            return file       
        
        filename = settings.BASE_DIR / file.file.name

        os.remove(filename)
        file.delete()

        return Response({
            'message': 'Файл удален',
        }, status=200)


class DownloadFileView(Protected, APIView):
    def get(self, request, pk):
        user = get_token_from_request(request)

        file = does_user_has_file(user, pk)

        if type(file) == Response:
            return file       
        
        filename = settings.BASE_DIR / file.file.name

        return FileResponse(open(filename, "rb"))
