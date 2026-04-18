from django.urls import path
from .views import CommunityCreateView, CommunityListView

urlpatterns = [
    path('create-community/', CommunityCreateView.as_view(), name='community-create'),
    path('list-communities/', CommunityListView.as_view(), name='community-list'),
]