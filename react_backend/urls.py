from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('reactapp.urls')),  # Add this line
     path('', include('reactapp.urls'))

]

