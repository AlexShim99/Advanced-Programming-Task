#!/usr/bin/python3

from account import Account
from decimal import Decimal

account1 = Account('Alex',Decimal('50.00'))
account1.deposit(Decimal(25))
print(account1.balance)

account2 = Account('Beta',Decimal('50.00'))
account2.deposit(Decimal(15))
print(account2.balance)
