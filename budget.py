class Category:

    name = None
    ledger = None

    def __init__(self, name):
        self.name = name
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
        self.withdraw(amount, "Transfer to " + other.name)
        # Deposit the money in the other Category
        other.deposit(amount, "Transfer from " + self.name)
        return True

    # Check if there are enough funds
    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False

    # Printing
    def __str__(self):
        # Add title bar to output string
        output_str = self.name.center(30, "*")
        # Add withdrawals and deposits to output string
        for elem in self.ledger:
            value = list(elem.values())[0]
            value = "{:.2f}".format(float(value))[:7]
            descr = list(elem.values())[1][:23]
            item = '\n' + descr + value.rjust(30 - len(descr))
            output_str += item
        # Add total to output string
        output_str += "\nTotal: " + str(self.get_balance())
        return output_str
    
    # Get total expenses
    def money_spent(self):
        # Get a list of all expenses (negative values in ledger)
        # and return an absolute sum of them
        return abs(sum([elem['amount'] for elem in self.ledger if elem['amount'] < 0.]))

# Method for creating a chart of expenses
def create_spend_chart(categories):
    # A variable containing a chart to return
    chart = "Percentage spent by category"
    # Get total money spent in all categories
    total = sum([elem.money_spent() for elem in categories])
    # A dictionary holding a percentages of expenses per category
    percentage = {}
    for category in categories:
        percentage[category.name] = 100 * category.money_spent() / total
    # Create y axis and fill the histogram
    for iperc in range(100,-10,-10):
        chart += '\n' + str(iperc).rjust(3) + "|"
        for category in categories:
            if percentage[category.name] > iperc:
                chart += " o "
            else:
                chart += "   "
        chart += " "
    # Add a separation bar
    chart += '\n' + "    " + 3 * len(categories) * '-' + '-'
    # Add x axis to the histogram
    for ichar in range(max([len(elem.name) for elem in categories])):
        chart += '\n' + "    "
        for category in categories:
            if len(category.name) > ichar:
                chart += " " + category.name[ichar] + " "
            else:
                chart += "   "
        chart += " "
    
    return chart