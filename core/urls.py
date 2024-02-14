from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contact.urls')),
    path('', include('main.urls', namespace='default_1')),
    path('', include('blog.urls', namespace='default_2')),
    path('', include('about.urls')),
    path('', include('gallery.urls')),
    path('', include('adoption.urls')),
    path('', include('our_services.urls'))
]


urlpatterns += i18n_patterns(
    path('', include('main.urls')),
    path('', include('blog.urls')),
)



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)