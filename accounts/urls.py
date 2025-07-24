from django.urls import path

from .views import UserViewSet

app_name = 'accounts'

urlpatterns = [
    path('users/', UserViewSet.as_view({'post': 'create'}), name='user-list'),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'update'}), name='user-detail'),
]