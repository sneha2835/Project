from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ExpBudApp.finance_views import BudgetViewSet, TransactionViewSet
from ExpBudApp.views.auth_views import RegisterView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'budget', BudgetViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    # Authentication Routes
    path('auth/register/', RegisterView.as_view(), name="register"),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),

    #  Finance Routes
    path('finance/', include(router.urls)),  
]
