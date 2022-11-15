from django.contrib import admin
# from django.conf.urls import handle404, handle505
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api/', include('api.urls'))
]


handle404 = 'core.views.handle_404'
handle505 = 'core.views.handle_500'

