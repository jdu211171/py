class Account:
    """A class that represents bank account."""
    def __init__(self, id: str, name: str, balance: int = 0):
        self.id = id
        self.name = name
        self.balance = balance

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def set_balance(self, new_balance):
        self.balance = new_balance

    def credit(self, amount: int):
        self.set_balance(self.get_balance() + amount)
        return self.get_balance()

    def debt(self, amount: int):
        if amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
        else:
            print('Amount exceeded balance')
            return self.get_balance()

    def transfer_to(self, obj, amount: int):
        if amount <= self.get_balance():
            if isinstance(obj, Account) and amount:
                obj.set_balance(obj.get_balance() + amount)
                self.set_balance(self.get_balance() - amount)
        else:
            print('Amount exceeded balance')
            return self.get_balance()

    def to_string(self):
        return f'Account[id={self.id}, name={self.get_name()}, balance={self.get_balance()}]'



