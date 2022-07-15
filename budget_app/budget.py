class Category:
    def __init__(self, cat) -> None:
        self.cat = cat
        self._balance = 0
        self._ledger = []
        
    @property
    def ledger(self):
        return self._ledger
    
    def add_ledger(self, amount, description, neg=False):
        try:
            amount = float(amount)
        except:
            return None
        amount = -amount if neg else amount
        obj = {"amount": round(amount, 2), "description": description}
        self._ledger.append(obj)
        
    @property
    def balance(self):
        return round(self._balance, 2)
    
    def change_balance(self, amount, neg=False):
        try: 
            amount = float(amount)
        except:
            amount = 0
        amount = -amount if neg else amount
        self._balance += amount
    
    def deposit(self, amount, description="") -> None:
        self.add_ledger(amount, description)
        self.change_balance(amount)
    
    def withdraw(self, amount, description="") -> bool:
        if self.check_funds(amount):
            self.add_ledger(amount, description, neg=True)
            self.change_balance(amount, neg=True)
            return True
        return False
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, budget):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget.cat}")
            budget.deposit(amount, f"Transfer from {self.cat}")
            return True
        return False
    
    def check_funds(self, amount):
        if amount > self._balance:
            return False
        return True
    
    def __str__(self):
        first_line = "*" * int((30 - len(self.cat)) / 2) + self.cat + \
            "*" * (30 - len(self.cat) - int((30 - len(self.cat)) / 2)) + "\n"
        lines = [first_line]
        total = 0
        for i, item in enumerate(self.ledger):
            descr = item["description"][:23] if len(item["description"]) > 23 else item["description"]
            value = f"{item['amount']:.2f}"
            spaces = " " * (30 - len(descr) - len(value))
            lines.append(descr + spaces + value + "\n")
            total += item["amount"]
        lines.append(f"Total: {total:.2f}")
        final_text = ""
        for line in lines:
            final_text += line 
        return final_text
    
def create_spend_chart(categories):
    totals = []
    pct = []
    lines = []
    final_text = ""
    for item in categories:
        totals.append(sum([abs(i["amount"]) for i in item.ledger if (i["amount"] < 0)]))
    total = sum(totals)
    pct = [int(int(value * 10 / total) * 10) for value in totals]
    lines.append("Percentage spent by category\n")
    for num in range(100, -1, -10):
        bar = " " * (3 - len(str(num))) + str(num) +  "| "
        for i, item in enumerate(pct):
            spaces = "   " if i < len(pct) - 1 else "   \n"
            label = "o  " if i < len(pct) - 1 else "o  \n"
            bar += label if item >= num else spaces
        lines.append(bar)
    lines.append(" " * 4 + "-" * (len(pct) * 3 + 1) + "\n")
    names = [item.cat for item in categories]
    max_name_len= max([len(name) for name in names])
    for i in range(max_name_len):
        name = " " * 5
        for j, item in enumerate(names):
            name += f"{item[i]}  " if i <= len(item) - 1 else "   "
        name += "\n" if i < len(item) - 1 else ""
        lines.append(name)
    for line in lines:
        final_text += line 
    return final_text
