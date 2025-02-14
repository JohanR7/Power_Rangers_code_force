from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("location/", views.location, name="location"),
    path("earth/", views.earth, name="earth"),
    path("form/", views.form_view, name="form"),
    path("analytics/",views.analytics,name="analytics")
]
