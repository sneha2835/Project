from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BudgetViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'budget', BudgetViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
