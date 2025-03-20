from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now  # Import this to use default datetime

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    transaction_date = models.DateField(default=now)  # Use default=now instead of auto_now_add
    transaction_time = models.TimeField(default=now)  # FIX: Default value to avoid migration issue
    merchant_name = models.CharField(max_length=100, null=True, blank=True)
    payment_method = models.CharField(
        max_length=50,
        choices=[
            ('Cash', 'Cash'),
            ('Credit Card', 'Credit Card'),
            ('Debit Card', 'Debit Card'),
            ('UPI', 'UPI'),
            ('Other', 'Other')
        ],
        default='Cash'
    )
    transaction_description = models.TextField(null=True, blank=True)
    id = models.BigAutoField(primary_key=True)

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    budget_limit = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=now)  # FIX: Default value added
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
    prediction_date = models.DateField(default=now)  # FIX: Default value added
    prediction_type = models.CharField(
        max_length=50,
        choices=[
            ('Expense Forecast', 'Expense Forecast'),
            ('Savings Forecast', 'Savings Forecast'),
            ('Anomaly Detection', 'Anomaly Detection')
        ],
        default='Expense Forecast'
    )
    confidence_score = models.FloatField(null=True, blank=True)
    id = models.BigAutoField(primary_key=True)

class OverspendingAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    alert_type = models.CharField(max_length=50, choices=[
        ('Overspending', 'Overspending'),
        ('Unusual Transaction', 'Unusual Transaction')
    ], default='Overspending')
    alert_message = models.TextField()
    alert_date = models.DateTimeField(default=now)  # FIX: Default value added

    def __str__(self):
        return f"{self.user.email} - {self.category} - {self.alert_type}"

class FinancialReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=50, choices=[
        ('Monthly Summary', 'Monthly Summary'),
        ('Yearly Report', 'Yearly Report')
    ], default='Monthly Summary')
    report_data = models.JSONField()
    generated_at = models.DateTimeField(default=now)  # FIX: Default value added

    def __str__(self):
        return f"{self.user.email} - {self.report_type}"

class RecurringTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    start_date = models.DateField(default=now)  # FIX: Default value added
    frequency = models.CharField(
        max_length=50,
        choices=[
            ('Daily', 'Daily'),
            ('Weekly', 'Weekly'),
            ('Monthly', 'Monthly'),
            ('Yearly', 'Yearly')
        ],
        default='Monthly'
    )
    id = models.BigAutoField(primary_key=True)
