from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, MenuItemViewSet, CustomerOrderViewSet,AssignUserToManagerGroup, AssignToDeliveryCrew, DeliveryCrewOrderView

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('menu-items', MenuItemViewSet, basename='menu-items')
router.register('orders', CustomerOrderViewSet, basename='orders')

urlpatterns = [
    path('', include(router.urls)),
    path('assign-manager/', AssignUserToManagerGroup.as_view(), name='assign-manager'),
    path('assign-delivery-crew/', AssignToDeliveryCrew.as_view(), name='assign-delivery-crew'),
    path('delivery-orders/', DeliveryCrewOrderView.as_view(), name='delivery-orders'),
]