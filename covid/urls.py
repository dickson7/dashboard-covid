"""covid URL Configuration
"""
#Django
from django.contrib import admin
from django.urls import path

from covid import views as local_views
from covid19 import views as covid_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('users/login', users_views.login_view, name='login'),
    path('users/logout', users_views.logout_view, name='logout'),
    path('users/signup', users_views.signup, name='signup'),

    path('hi/', local_views.hi, name='test'),

    path('dashboard/', covid_views.details_covid, name= 'dashboard'),
    path('dashboard/country', covid_views.details_country, name= 'country'),
   
]