from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard),
    # path('about/',views.about),
    path('hello/<str:username>',views.hello_params),
]