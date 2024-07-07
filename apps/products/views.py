from django.views.generic import ListView, DetailView
from apps.products.models import Product
from apps.basket.models import Basket


class ProductListView(ListView):
    model = Product
    template_name = 'products.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['user_cart'] = Basket.objects.filter(user_id=self.request.user.id).values_list('product_id', flat=True)
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'

