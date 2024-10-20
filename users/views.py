from rest_framework import generics, viewsets, status, views, permissions
from .models import CustomUser
from rest_framework.response import Response
from .serializers import CustomUserSerializer, LoginSerializer
from django.contrib.auth import authenticate, login
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user": CustomUserSerializer(user, context=self.get_serializer_context()).data,
                "message": "User Created Successfully.",
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            user_data = CustomUserSerializer(user, context={'request': request}).data
            return Response({
                "user": user_data,
                "message": "User Logged In Successfully",
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)