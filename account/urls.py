from django.urls import path, include
from account.views import AccountListView, AccountCreateView



urlpatterns = [
    path('accounts/', AccountListView.as_view(), name='all-accounts'),
    path('account/create/', AccountCreateView.as_view(), name='create-lot'),
]

