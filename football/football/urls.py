from django.contrib import admin
from django.urls import path, include

admin.site.index_title = 'Desktop'
admin.site.site_header = 'Football Club Admin'
admin.site.site_title = 'Football Club Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
