from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    # Add other URL patterns for your links here
    # app
    path('app/', include('app.urls')),
    
]
