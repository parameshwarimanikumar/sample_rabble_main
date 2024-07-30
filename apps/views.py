# apps/views.py
from django.shortcuts import render
from apps.account.models import Account  # Import the Account model

def account_list(request):
    accounts = Account.objects.all()  # Retrieve all Account objects from the database
    context = {
        'accounts': accounts  # Pass accounts queryset to the template
    }
    return render(request, 'account_list.html', context)

def api_response(request):
    # Your existing view logic for api_response
    return render(request, 'api_response.html', {})
