from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from .import views
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static



schema_view = get_schema_view(
   openapi.Info(
      title="  Documentation for the authentication api",
      default_version='v1',
      description="This the the Api documentation for the authentication api ",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('account.urls'),),
    path('',views.index,name="index" ),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

