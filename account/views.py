from rest_framework import generics
from account.serializers import AccountListSerializer, AccountDetailSerializer
from account.models import Account


class AccountCreateView(generics.CreateAPIView):
    """Создание аккаунта"""
    serializer_class = AccountDetailSerializer


class AccountListView(generics.ListAPIView):
    """Все пользователи"""
    serializer_class = AccountListSerializer
    queryset = Account.objects.all()
    permission_classes = ()