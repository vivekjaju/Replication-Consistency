from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('order/', include('replication.urls')),
    # path('buy/', include('replication.urls')),
    path('admin/', admin.site.urls),
]