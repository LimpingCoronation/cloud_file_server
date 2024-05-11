from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from file_manager.mixins import Protected


class Logout(Protected, APIView):
    def post(self, request):
        token = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'].split(' ')[1])
        token.delete()

        return Response(status=200)
