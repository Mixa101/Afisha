from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
import random

from .models import ConfirmationCode
from .serializer import RegistrationSerializer, LoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=False)
        confirmation_code = random.randint(100000, 999999)
        ConfirmationCode.objects.create(user=user, code=confirmation_code)
        Token.objects.create(user=user)
        
        print(f"Код подтверждения для пользователя {user.username}: {confirmation_code}")


@api_view(['POST'])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        code = request.data.get('code')

        try:
            user = User.objects.get(username=username)
            confirmation = ConfirmationCode.objects.get(user=user, code=code)

            user.is_active = True
            user.save()

            confirmation.delete()
            return Response({"message": "Пользователь успешно подтвержден."}, status=status.HTTP_200_OK)

        except (User.DoesNotExist, ConfirmationCode.DoesNotExist):
            return Response({"error": "Неверный код подтверждения или имя пользователя."},
                            status=status.HTTP_400_BAD_REQUEST)
