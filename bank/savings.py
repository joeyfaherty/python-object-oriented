from .account import Account


class SavingsAccount(Account):
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.02) -> None:
        super().__init__(owner, balance)
        self.interest_rate: float = interest_rate

    def apply_interest(self) -> None:
        interest = self._balance * self.interest_rate
        self.deposit(interest)
