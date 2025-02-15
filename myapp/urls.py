from django.urls import path
from . import views
from .views import home, signup_view, login_view, logout_view
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', home, name='home'),
    path("location/", views.location, name="location"),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path("earth/", views.earth, name="earth"),
    path("form/", views.form, name="form"),
    path("analytics/",views.analytics,name="analytics"),
    path("get_suggestions/", views.get_gemini_suggestions, name="get_gemini_suggestions"),
]
