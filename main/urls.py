from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('delivery/', DeliveryView.as_view(), name='delivery'),
    path('trade-in/', TradeinView.as_view(), name='trade-in'),
    path('warranty/', WarrantyView.as_view(), name='warranty'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
    path('details/', DetailsView.as_view(), name='details'),
    path('thanks/', RequestsView.as_view(), name='thanks'),
    path('<slug:category>/', CategoryView.as_view()),
    path('<slug:category>/<slug:name>', ProductView.as_view()),
    path('<slug:category>/categories/<slug:undercat>/', UnderCategoryView.as_view()),

]