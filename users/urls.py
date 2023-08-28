from django.urls import path,include
from rest_framework.routers import DefaultRouter
from users.views import ClientView,AdminView,MyObtainTokenView

router = DefaultRouter()
router.register(r'clients',ClientView,basename="clients")
router.register(r'admins',AdminView,basename="admins")

urlpatterns = [
    path("",include(router.urls)),
    path('token/',MyObtainTokenView.as_view() , name='token_obtain_pair')
]
