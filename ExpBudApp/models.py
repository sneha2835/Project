from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass  # You can add custom fields if needed

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    transaction_date = models.DateField()
    id = models.BigAutoField(primary_key=True)

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    budget_limit = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.BigAutoField(primary_key=True)

class SavingsGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_savings = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deadline = models.DateField()
    id = models.BigAutoField(primary_key=True)

class AIPrediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    predicted_expense = models.DecimalField(max_digits=10, decimal_places=2)
    prediction_date = models.DateField()
    id = models.BigAutoField(primary_key=True)
