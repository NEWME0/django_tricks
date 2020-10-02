from django.contrib import admin
from django.urls import path, include

from .settings import DEBUG


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls'))
]


if DEBUG:
    from rest_framework.permissions import AllowAny
    from drf_yasg.openapi import Info
    from drf_yasg.views import get_schema_view

    info = Info(title='Tricks API', default_version='0.0.1', description='API description')
    schema_view = get_schema_view(info, permission_classes=(AllowAny,), public=True,)
    swagger_view = schema_view.with_ui('swagger', cache_timeout=0)

    urlpatterns += [
        path('', swagger_view)
    ]
