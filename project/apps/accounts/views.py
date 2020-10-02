from rest_framework.generics import ListCreateAPIView

from .models import Scope, Role
from .serializers import ScopeSerializer, RoleSerializer


class ScopeListCreateView(ListCreateAPIView):
    serializer_class = ScopeSerializer
    queryset = Scope.objects.all()


class RoleListCreateView(ListCreateAPIView):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
