from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('newsletter', views.newsletter, name='newsletter'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_and_conditions/', views.terms_and_conditions,
         name='terms_and_conditions'),
    path('return_and_refund_policy/', views.return_and_refund_policy,
         name='return_and_refund_policy'),
]
