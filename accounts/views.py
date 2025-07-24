from rest_framework import viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView as TokenRefreshViewBase

from .models import User
from .permissions import IsOwnerOrReadOnly
from .serializers import UserCreateSerializer, UserUpdateSerializer, SignInSerializer, TokenRefreshSerializer


class LoginAPIView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SignInSerializer


class TokenRefreshView(TokenRefreshViewBase):
    serializer_class = TokenRefreshSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserUpdateSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
