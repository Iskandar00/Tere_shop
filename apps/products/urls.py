from django.urls import path

from apps.products.views import ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list-page'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail-page'),
]
