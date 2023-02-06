#!/usr/bin/python3

from decimal import Decimal

class Account:
    def __init__(self, name, balance):
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00')

        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self.balance += amount

