"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
import drf_spectacular.views as views_spect
# from abcdef import urls as abcdef_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('api/v1/abcdef/', include(abcdef_urls)),

    # swagger
    path('api/schema/',
         views_spect.SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',
         views_spect.SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/',
         views_spect.SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
