from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .auth import RegisterView
from .views import ProfileView


app_name = "users"
urlpatterns = [
    path('register/', RegisterView.as_view(), name='registration'),
    path('<username>/', ProfileView.as_view(), name='user_profile'),
]
