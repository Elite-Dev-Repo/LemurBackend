
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from core.views import UserCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/register/', UserCreateView.as_view(), name='user_create'),




    # API 

    path('api/', include('community.urls')),
    path('api/', include('core.urls')),
    path('api/', include('reactions.urls')),


]
