from django.urls import path

from product.apps import ProductConfig
from product.views import contacts, ProductView, ProductListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, ProductUpdateWithVersionView

app_name = ProductConfig.name

urlpatterns = [
    path('', ProductView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),

    path('list/', ProductListView.as_view(), name='list'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<str:pk>/', ProductUpdateView.as_view(), name='update'),
    path('update/<str:pk>/version/', ProductUpdateWithVersionView.as_view(), name='update_with_version'),
    path('delete/<str:pk>/', ProductDeleteView.as_view(), name='delete'),

#    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),

#    path('status/<int:pk>/', change_status, name='status'),
]
