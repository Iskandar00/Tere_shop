from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.general.urls')),
    path('users/', include('apps.users.urls')),
    path('basket/', include('apps.basket.urls')),
    path('products/', include('apps.products.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
