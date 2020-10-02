from django.urls import path

from .views import *


urlpatterns = [
    path('scopes/', ScopeListCreateView.as_view()),
    path('roles/', RoleListCreateView.as_view()),
]
