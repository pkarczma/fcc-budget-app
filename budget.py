class Category:

    category_name = None
    ledger = None

    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []

    # Deposit method
    def deposit(self, amount, description = ""):
        self.ledger.append({ "amount" : amount, "description" : description })

    # Withdrawal method
    def withdraw(self, amount, description = ""):
        # Do not withdraw money if there are not enough funds
        if not self.check_funds(amount):
            return False
        # Do the withdrawal if there are enough funds
        self.ledger.append({ "amount" : -amount, "description" : description })
        return True

    # Get the money balance
    def get_balance(self):
        return sum([elem['amount'] for elem in self.ledger])

    # Transfer method
    def transfer(self, amount, other):
        # Cancel the transfer if there are not enough funds
        if not self.check_funds(amount):
            return False
        # Withdraw the money from this category
        self.withdraw(amount, "Transfer to " + other.category_name)
        # Deposit the money in the other Category
        other.deposit(amount, "Transfer from " + self.category_name)
        return True

    # Check if there are enough funds
    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False

    # Printing
    def __str__(self):
        
        output = self.category_name.center(30, "*")

        for elem in self.ledger:
            value = list(elem.values())[0]
            value = "{:.2f}".format(float(value))[:7]
            descr = list(elem.values())[1][:23]
            item = '\n' + descr + value.rjust(30 - len(descr))
            output += item
        
        output += "\nTotal: " + str(self.get_balance())
        return output

def create_spend_chart(categories):
    return