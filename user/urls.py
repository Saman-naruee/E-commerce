from django.urls import path
from .views import UserProfileView, UserListView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
