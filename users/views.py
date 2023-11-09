from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework import generics
from users.serializers import UserSerializer
from users.models import User
# Create your views here.


class UserCreateAPIView(generics.CreateAPIView):
    """
    Эндпоинт для регистрации пользователя
    """
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserMeAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        try:
            obj = User.objects.get(pk=self.request.user.id)
            return obj
        except ObjectDoesNotExist:
            raise Http404
