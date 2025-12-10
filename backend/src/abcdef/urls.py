from django.urls import include, path
from rest_framework import routers
# import abcdef.views as abcdef_views

# router = routers.SimpleRouter()
# router.register(r'phones', abcdef_views.AbcdefModelViewSet, basename='abcdef-phones')

# urlpatterns = [
#     path('', include(router.urls)),
#     path('phone-search/<str:query>/', abcdef_views.PhoneSearchView.as_view(), name='phone-search'),
# ]

# https://opendata.digital.gov.ru/api/v1/abcdef/phone?num=9529157408&limit=50