from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Cambiar la url en caso de querer agregar una ruta que le precedan los de landingpage
    path('',include('landingpage.urls'))
]
