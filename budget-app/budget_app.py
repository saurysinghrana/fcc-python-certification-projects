"""
Budget App

A budget management application built as part of the
freeCodeCamp Scientific Computing with Python certification.
"""


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append(
            {
                "amount": amount,
                "description": description,
            }
        )

    def get_balance(self):
        balance = 0

        for item in self.ledger:
            balance += item["amount"]

        return balance

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append(
                {
                    "amount": -amount,
                    "description": description,
                }
            )
            return True

        return False

    def transfer(self, amount, category):
        if self.withdraw(amount, "Transfer to " + category.name):
            category.deposit(amount, "Transfer from " + self.name)
            return True

        return False

    def __str__(self):
        output = self.name.center(30, "*") + "\n"

        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = f"{item['amount']:.2f}"[:7].rjust(7)

            output += description + amount + "\n"

        output += f"Total: {self.get_balance():.2f}"

        return output


def create_spend_chart(categories):
    spending = []

    for category in categories:
        total = 0

        for item in category.ledger:
            if item["amount"] < 0:
                total += abs(item["amount"])

        spending.append(total)

    total_spent = sum(spending)

    percentages = []

    for amount in spending:
        percentage = (amount / total_spent) * 100
        percentage = int(percentage // 10) * 10
        percentages.append(percentage)

    chart = "Percentage spent by category\n"

    for level in range(100, -1, -10):
        chart += f"{level:>3}| "

        for percent in percentages:
            if percent >= level:
                chart += "o  "
            else:
                chart += "   "

        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    names = [category.name for category in categories]
    max_length = max(len(name) for name in names)

    for i in range(max_length):
        chart += "     "

        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "

        chart += "\n"

    return chart.rstrip("\n")


if __name__ == "__main__":
    food = Category("Food")
    clothing = Category("Clothing")
    entertainment = Category("Entertainment")

    food.deposit(1000, "Initial deposit")
    food.withdraw(15.89, "Groceries")
    food.withdraw(25.55, "Restaurant")

    clothing.deposit(500, "Initial deposit")
    clothing.withdraw(75.25, "Jeans")

    entertainment.deposit(800, "Initial deposit")
    entertainment.withdraw(120, "Movie tickets")

    print(food)
    print()
    print(clothing)
    print()
    print(entertainment)
    print()
    print(create_spend_chart([food, clothing, entertainment]))
