from abc import ABC, abstractmethod
class Payment(ABC):
    def print_slip(self, amount):
        print("Your purchase amount: ",amount)

    @abstractmethod
    def payment(self, amount):
         pass

class DebitCardPayment(Payment):
    def payment(self, amount):
        print('Your debit card purchase amount of {} exceeded your $100 limit '.format(amount))


obj = DebitCardPayment()
obj.print_slip("$400")
obj.payment("$400")
