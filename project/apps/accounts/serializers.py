from ..abstract.serializers import *
from .models import *


__all__ = ['ScopeSerializer', 'RoleSerializer']


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


class ServiceSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class AccountSerializer(DynamicFieldsModelSerializer):
    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['service'] = ServiceSerializer().to_representation(instance.service)
        result['roles'] = RoleSerializer(many=True).to_representation(instance.roles)
        return result

    class Meta:
        model = Account
        fields = '__all__'
