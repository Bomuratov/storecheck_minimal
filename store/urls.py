from django.urls import path

from store import views


urlpatterns = [
    path('home', views.index, name='home'),
    path('create_sku', views.create_sku, name='create_sku'),
    path('create_trade', views.create_trade, name='create_trade'),
    path('create_territory', views.create_territory, name='create_territory'),
    path('edit_sku/<int:pk>', views.edit_sku, name='edit_sku'),
    path('del_sku/<int:pk>', views.del_sku, name='del_sku')
]
