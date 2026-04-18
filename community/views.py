from django.shortcuts import render
from .serializers import CommunitySerializer
from .models import Community
from rest_framework.generics import  ListAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

# Create your views here.

class CommunityCreateView(CreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = (IsAdminUser)



class CommunityListView(ListAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = (IsAuthenticatedOrReadOnly)