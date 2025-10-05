from .account import Account


class CurrentAccount(Account):
    def __init__(self, owner: str, balance: float = 0.0, overdraft_limit: float = 100.0) -> None:
        super().__init__(owner, balance)
        self.overdraft_limit: float = overdraft_limit

    def withdraw(self, amount: float) -> None:
        if amount > self._balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded.")
        self._balance -= amount
