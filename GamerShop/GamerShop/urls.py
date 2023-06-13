from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('about/', include('main.urls')),
    path('product/',include('main.urls')),
    path('video/',include('main.urls')),
    path('remot/',include('main.urls')),
    path('contact/',include('main.urls')),
    path('product/<int:id>',include('main.urls')),
    path('videogames/<int:id>',include('main.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
