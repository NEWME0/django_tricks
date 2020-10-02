from ..abstract.serializers import *
from .models import Scope, Role


class ScopeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Scope
        fields = '__all__'


class RoleSerializer(DynamicFieldsModelSerializer):
    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['scopes'] = ScopeSerializer(many=True).to_representation(instance.scopes)
        return result

    class Meta:
        model = Role
        fields = '__all__'
