from rest_framework import viewsets, generics
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
  # Task 4: Create API Views
  ## View to list all users
  # class UsersList(generics.ListAPIView):
  #   queryset = User.objects.all()
  #   serializer_class = UserSerializer

  ## View to retrieve a user by ID:
  # class UserDetail(generics.RetrieveAPIView):
  #   queryset = User.objects.all()
  #   serializer_class = UserSerializer

  # Task 5: Create API URLs
  # Use the DefaultRouter from DRF for automatic URL routing.
  queryset = User.objects.all()
  serializer_class = UserSerializer