from django.urls import path, include
# DefaultRouter from DRF for automatic URL routing
from rest_framework.routers import DefaultRouter 
from .views import UserViewSet 

# DefaultRouter is typically used with viewsets, 
# which combine the logic for multiple related views into a single class. 
# Create a router and were we can register our viewsets.
router = DefaultRouter()

# register the UserViewSet 
router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
  # Create URLs for the views you created in Task 4. (no longer need after using DefaultRouter)
  # path('api/users/', UsersList.as_view(), name='users-list'),
  # path('api/users/<int:pk>/', UserDetail.as_view(), name='user-detail'),

  path('api/', include(router.urls)),
]