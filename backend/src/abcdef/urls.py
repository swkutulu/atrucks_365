from django.urls import include, path, re_path
from rest_framework import routers
from abcdef import views as abcdef_views

router = routers.SimpleRouter()
# router.register(r'phones', abcdef_views.PhoneModelViewSet, basename='abcdef-phones')
router.register(r'info', abcdef_views.DownloadInfoModelViewSet, basename='abcdef-info')

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^phone-search/(?P<phone>[0-9]{10,11})/', abcdef_views.PhoneSearchView.as_view(), name='phone-search'),
    re_path(r'^phone-norm-search/(?P<phone>[0-9]{10,11})/', abcdef_views.PhoneNormSearchView.as_view(), name='phone-norm-search'),
]

# https://opendata.digital.gov.ru/api/v1/abcdef/phone?num=9529157408&limit=50