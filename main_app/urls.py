from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('months/', views.months_index, name='months_index'),
  path('months/<int:month_id>/', views.months_detail, name='months_detail'),
]