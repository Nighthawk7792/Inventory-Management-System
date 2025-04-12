import os
import sys
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory.settings')

try:
    execute_from_command_line(['manage.py', 'runserver'])
except Exception as e:
    print(f"Error: {e}")
    input("Press Enter to exit...")