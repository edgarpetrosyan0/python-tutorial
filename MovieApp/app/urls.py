from django.contrib import admin
from django.urls import path,include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.urls import path

from app import settings

schema_view = get_schema_view(
   openapi.Info(
        title="Movie API",
        default_version='v3',
        description="API documentation for managing movie",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),        
    path('accounts/', include('accounts.urls')), 
    path('products/', include('products.urls')),  
    path('blogs/', include('blogs.urls')), 

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 