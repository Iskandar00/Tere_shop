from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from apps.basket.models import Basket
from django.contrib.auth.mixins import LoginRequiredMixin


class BaskedListView(LoginRequiredMixin, ListView):
    template_name = 'basket.html'

    def get_queryset(self):
        return Basket.objects.filter(user_id=self.request.user.pk)
    

class CreateOrDeleteBasked(LoginRequiredMixin, View):
    def get(self, request, pk):
        product_id = pk
        user = request.user

        basket, create = Basket.objects.get_or_create(user_id=user.pk, product_id=product_id)

        if not create:
            basket.delete()
        return redirect(request.META['HTTP_REFERER'])