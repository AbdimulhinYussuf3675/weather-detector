from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('weather.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    
]
