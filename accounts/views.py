from rest_framework import viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import UserSerializer, SignInSerializer


class LoginAPIView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SignInSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


