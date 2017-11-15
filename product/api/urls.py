from __future__ import absolute_import
from django.conf.urls import url
from product.api.views import (
    ProductListAPIView,
    ProductDetailAPIView,
    ProductDeleteAPIView,
    ProductUpdateAPIView,
    ProductCreateAPIView
)
urlpatterns = [

    url(r'^create/$', ProductCreateAPIView.as_view(), name='APIcreate'),
    url(r'^$', ProductListAPIView.as_view(), name='APIList'),
    url(r'^(?P<pk>[0-9]+)/$', ProductDetailAPIView.as_view(), name='APIDetail'),
    url(r'^(?P<pk>[0-9]+)/update/$', ProductUpdateAPIView.as_view(), name='APIupdate'),
    url(r'^(?P<pk>[0-9]+)/delete/$', ProductDeleteAPIView.as_view(), name='APIdelete'),
]
