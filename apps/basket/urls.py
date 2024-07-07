from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.CreateOrDeleteBasked.as_view(), name='create_or_delete_basked'),
    path('', views.BaskedListView.as_view(), name='basked'),

]