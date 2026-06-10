#!/usr/bin/env python3
class CashRegister: 
    def __init__(self,discount=0):

        self.items=[]
        self.previous_transactions=[]
        self.total=0
        self.discount=discount

    @property #this is the getter
    def discount(self):
        return self._discount

    @discount.setter # this is the setter   
    def discount(self,value):
            if isinstance(value,int) and 0<=value<=100:
                self._discount=value
            else:
                print("Not valid discount")
                self._discount=0

    def add_item(self,item,price,quantity=1):
        item_total_price=price*quantity
        self.total+=item_total_price # this is the actuak price before discount

        for n in range(quantity):
            self.items.append(item)

        transactions={
            "item": item,
            "price":price,
            "quantity":quantity
        }                    
        self.previous_transactions.append(transactions)# this basically stores the dictionaries
 
    def apply_discount(self):
        if not self.previous_transactions or self.discount==0:
            print("There is no discount to apply.")  
            return

        last_transaction=self.previous_transactions.pop() 
        item_name=last_transaction["item"]
        self.items.remove(item_name)

        original_total_amount=last_transaction["price"]*last_transaction["quantity"]
        self.total-=original_total_amount

        discount_factor = 1 - (self.discount / 100)
        discounted_item_total=original_total_amount*discount_factor
        self.total+=discounted_item_total
        self.items.append(item_name)  
        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void")
            return
        last_transaction=self.previous_transactions.pop()    

        void_amount= last_transaction["price"]*last_transaction["quantity"]
        self.total-=void_amount

        for _ in range (last_transaction["quantity"]):
            if last_transaction["item"] in self.items:
                self.items.remove(last_transaction["item"])    