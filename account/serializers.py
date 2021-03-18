from rest_framework import serializers
from account.models import Account

class AccountDetailSerializer(serializers.ModelSerializer):
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    password = serializers.CharField(
        style={'input_type': 'password'}
    )

    class Meta:
        model = Account
        fields = '__all__'


class AccountListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'