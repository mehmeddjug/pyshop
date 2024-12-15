from django.shortcuts import get_object_or_404, redirect, render

from account.forms import AccountForm
from account.models import Account


# Register account
def register_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_accounts')
    else:
        form = AccountForm()
    return render(request, 'create_account.html', {'form': form})

# List accounts
def get_accounts(request):
    accounts = Account.objects.all()
    return render(
        request,
        'get_accounts.html',
        {'accounts': accounts}
    )

# Get account by primary key
def get_account_by_pk(request, pk):
    account = get_object_or_404(Account, pk=pk)
    return render(
        request,
        'get_account_by_pk.html',
        {'account': account}
    )

# Update account
def update_account_by_pk(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('get_accounts')
    else:
        form = AccountForm(instance=account)
    return render(request, 'update_account.html', {'form': form})

# Delete account
def delete_account_by_pk(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        account.delete()
        return redirect('get_accounts')
    return render(
        request,
        'delete_account.html',
        {'account': account}
    )
