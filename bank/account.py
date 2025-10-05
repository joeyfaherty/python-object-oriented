from __future__ import annotations
from typing import List


class Account:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner: str = owner
        self._balance: float = balance  # Protected by convention

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

    def get_balance(self) -> float:
        return self._balance

    def __repr__(self) -> str:
        return f"<Account(owner={self.owner!r}, balance={self._balance:.2f})>"
