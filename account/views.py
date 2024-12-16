from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render

from account.forms import AccountForm
from account.models import Account


def register_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_accounts')
    else:
        form = AccountForm()
    return render(request, 'create_account.html', {'form': form})


def get_accounts(request):
    accounts = Account.active.all()
    return render(
        request,
        'get_accounts.html',
        {'accounts': accounts}
    )


def get_account_by_id(request, id):
    account = get_object_or_404(Account.active, pk=id)
    return render(
        request,
        'get_account_by_id.html',
        {'account': account}
    )


def update_account_by_id(request, id):
    account = get_object_or_404(Account.active, pk=id)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('get_accounts')
    else:
        form = AccountForm(instance=account)
    return render(request, 'create_account.html', {'form': form})


def delete_account_by_id(request, id):
    account = get_object_or_404(Account.active, pk=id)
    if request.method == 'POST':
        account.is_deleted = True
        account.save()
        return redirect('get_accounts')
    return render(
        request,
        'delete_account.html',
        {'account': account}
    )


def restore_account(request, username):
    account = get_object_or_404(Account, username=username)
    if request.method == 'POST':
        account.is_deleted = False
        account.save()
        return redirect('get_accounts')
    return render(
        request,
        'restore_account.html',
        {'account': account}
    )
