#from django.contrib.auth.models import User, Group
#from rest_framework import viewsets
#from rest_framework import permissions
from lots.serializers import GroupSerializer, PagesDetailSerializer, CategoryDetailSerializer, CategoryFilterSerializer
from rest_framework import generics
from lots.serializers import LotsListSerializer, LotDetailSerializer, CategoryListSerializer, PagesSerializer
from lots.models import Lots, Account, Pages, Category, CategoryFilter
from lots.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class LotCreateView(generics.CreateAPIView):
    """Создание лотов"""
    serializer_class = LotDetailSerializer


class LotListView(generics.ListAPIView):
    """Все лоты"""
    serializer_class = LotsListSerializer
    queryset = Lots.objects.all()
    permission_classes = ()


class CategoryListView(generics.ListAPIView):
    """Все пользователи"""
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()
    permission_classes = ()


class PagesView(generics.ListAPIView):
    """Все пользователи"""
    serializer_class = PagesSerializer
    queryset = Pages.objects.all()
    permission_classes = ()


class PagesCreateView(generics.CreateAPIView):
    """Создание лотов"""
    serializer_class = PagesDetailSerializer


class LotDetailView(generics.RetrieveUpdateDestroyAPIView):
    """О лоте"""
    serializer_class = LotDetailSerializer
    queryset = Lots.objects.all()
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)


class CategoryDetailView(generics.RetrieveAPIView):
    """О Категории"""
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()


class CategoryFilterList(generics.ListAPIView):
    """Все лоты"""
    serializer_class = CategoryFilterSerializer
    queryset = CategoryFilter.objects.all()
    permission_classes = ()
# class GroupViewSet(viewsets.ModelViewSet):
#
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]


