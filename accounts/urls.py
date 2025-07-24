from django.urls import path

from .views import UserViewSet, LoginAPIView, TokenRefreshView

app_name = 'accounts'

urlpatterns = [
    path('signin', LoginAPIView.as_view(), name='signin'),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserViewSet.as_view({'post': 'create'}), name='user-list'),
    path('users/<int:pk>', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'update'}), name='user-detail'),
]
