from rest_framework.generics import *

from .models import *
from .serializers import *


class ScopeListCreateView(ListCreateAPIView):
    serializer_class = ScopeSerializer
    queryset = Scope.objects.all()


class ScopeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ScopeSerializer
    queryset = Scope.objects.all()


class RoleListCreateView(ListCreateAPIView):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()


class RoleRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
