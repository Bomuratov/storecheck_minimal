from django.urls import path

from excellApp import views

urlpatterns = [
    path('exprort/', views.export_xlsx, name='export')
]

