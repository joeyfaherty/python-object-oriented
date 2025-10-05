from bank.savings import SavingsAccount
from bank.current import CurrentAccount

def main() -> None:
    alice_savings = SavingsAccount("Alice", 1000.0, 0.03)
    bob_checking = CurrentAccount("Bob", 500.0, overdraft_limit=200.0)

    print(alice_savings)
    alice_savings.apply_interest()
    print("After interest:", alice_savings)

    print(bob_checking)
    bob_checking.withdraw(600.0)
    print("After withdrawal:", bob_checking)

if __name__ == "__main__":
    main()