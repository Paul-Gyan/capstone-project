from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet, LoginView

router = DefaultRouter()
router.register(r'register', RegisterViewSet, basename='register')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login')
]