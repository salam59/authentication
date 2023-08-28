from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from users.models import CustomUser
from users.serializers import UserSerializer,MyObtainTokenSerializer
from users.permissions import ClientPermissions,AdminPermissions
# Create your views here.

class ClientView(ModelViewSet):
    queryset = CustomUser.objects.filter(user_type='client')
    serializer_class = UserSerializer
    lookup_field = 'id'
    permission_classes = [ClientPermissions | AdminPermissions]
    allowed_user_type = 'client'

class AdminView(ModelViewSet):
    queryset = CustomUser.objects.filter(user_type='admin')
    serializer_class = UserSerializer
    lookup_field = 'id'
    permission_classes = [AdminPermissions]
    allowed_user_type = 'admin'

class MyObtainTokenView(TokenObtainPairView):
    serializer_class = MyObtainTokenSerializer