from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('months/', views.months_index, name='months_index'),
  path('months/<int:month_id>/', views.months_detail, name='months_detail'),
  path('months/create/', views.MonthCreate.as_view(), name='months_create'),
  path('months/<int:pk>/delete/', views.MonthDelete.as_view(), name='months_delete'),
  path('months/<int:month_id>/add_expense/', views.add_expense, name='add_expense'),
  path('accounts/signup/', views.signup, name='signup'),

]