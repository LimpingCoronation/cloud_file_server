from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class Protected:
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
