from django.conf.urls import url, include
from django.contrib import admin
from product import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^products/', include('product.urls')),
    url(r'api/products/', include('product.api.urls', namespace='APIProduct')),
    url(r'^$', views.product_home, name='product_list'),
]
