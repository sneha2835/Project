from rest_framework import viewsets  #  Add this import
from rest_framework.permissions import IsAuthenticated  #  Import permissions
from .models import Budget, Transaction
from .serializers import BudgetSerializer, TransactionSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]  # Require authentication

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]  # Require authentication
