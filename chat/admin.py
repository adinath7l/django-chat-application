# chat/admin.py
from django.contrib import admin
from .models import Message  # Import your Message model

admin.site.register(Message)  # Register the model
