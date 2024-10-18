from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-rule/', views.create_rule_api, name='create_rule'),
    path('evaluate-rule/', views.evaluate_rule, name='evaluate_rule'),
]

