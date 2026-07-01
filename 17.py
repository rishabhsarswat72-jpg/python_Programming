class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPal(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

p1 = CreditCard()
p2 = PayPal()

p1.pay(150)
p2.pay(200)