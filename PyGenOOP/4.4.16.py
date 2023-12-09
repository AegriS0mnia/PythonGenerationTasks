class BankAccount:
    def __init__(self, balance: int = 0):
        self._balance: int = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount: int):
        self._balance += amount

    def withdraw(self, amount: int):
        if self._balance - amount < 0:
            raise ValueError('На счете недостаточно средств')
        self._balance -= amount

    def transfer(self, account, amount: int):
        self.withdraw(amount)
        account.deposit(amount)
