
from django.contrib import admin
from django.urls import path,include,re_path

# for medias
from django.conf.urls.static import static
from django.conf import settings

#for deployment
from django.views.static import serve

urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('admin/', admin.site.urls),
    path('',include('newapp.urls')),
    path('users/',include('users.urls'))
]

#for deployment the below is commented and added in above list as re_path
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
