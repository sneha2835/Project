from django.contrib import admin
from .models import User, Budget, Transaction

admin.site.register(User)
admin.site.register(Budget)
admin.site.register(Transaction)
