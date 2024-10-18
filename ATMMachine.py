#Bharath goes to ATM Machine Center and withdraws 50000 from his account

#Objects:
# ATM Machine
# Card
# Money
# Bharath

class ATMMachine:

    def dispense_money(self,card, pin, amount):
       if pin == card.cardpin:
           if amount <= card.bank_balance:
            print("Dispensed amount:",amount)
            card.bank_balance -= amount
            return Money()
           else:
            print("Insufficient Funds")
            return None

class Card:
    def __init__(self):
        self.cardnum = 4869141523451121
        self.bank_balance = 100000
        self.cardpin = 1221 
class Money:
    pass

class Bharath:
    
    def withdraw(self):
        sbi_atm = ATMMachine()
        debit_card =Card() 
        m = sbi_atm.dispense_money(debit_card,1221,50000)
        print(type(m))
        print(f" Balance Amount in your bank Account: {debit_card.bank_balance}")

bh = Bharath()
bh.withdraw()