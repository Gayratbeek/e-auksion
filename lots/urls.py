from django.urls import path, include
from lots.views import LotCreateView, LotListView, LotDetailView, CategoryListView,\
    PagesView, PagesCreateView, CategoryDetailView, CategoryFilterList

app_name = 'lots'

urlpatterns = [
    path('lot/create/', LotCreateView.as_view(), name='create-lot'),
    path('all/', LotListView.as_view(), name='all-lots'),
    path('categories/', CategoryListView.as_view(), name='all-categories'),
    path('categories/filter', CategoryFilterList.as_view(), name='all-categories'),
    path('category/detail/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('pages/', PagesView.as_view(), name='pages-detail'),
    path('pages/create', PagesCreateView.as_view(), name='pages-create'),
    path('lot/detail/<int:pk>/', LotDetailView.as_view(), name='detail-lot'),
]