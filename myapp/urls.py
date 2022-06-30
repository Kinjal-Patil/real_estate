from django.urls import path

from myapp.views import Home

urlpatterns = [
    path('', Home.as_view(), name="home"),
]
