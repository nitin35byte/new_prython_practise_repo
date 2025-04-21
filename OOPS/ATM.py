class Atm:

    def __init__(self):
        self.pin = ''
        self.balance=0
        ##self.menu()
        print("id of self is :",id(self))

    def menu(self):
        user_input=input("""
        How can i help you
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anyting else to exit
        """)
        if user_input == '1':
            self.create_pin()

        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()

        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input('enter your pin')
        self.pin= user_pin
        user_balance= int(input('enter balance'))
        self.balance=user_balance
        print("pin create successfully")
        self.menu()

    def change_pin(self):
        old_pin= input('enter you old pin')
        if old_pin==self.pin:
            new_pin=input("enter new pin")
            self.pin=new_pin
            print("pin change successfully")
            self.menu()
        else:
            print("Try again u 2 more chance left")
            self.menu()
    def check_balance(self):
        user_pin=input('enter your pin')
        if user_pin==self.pin:
            print('your balance is',self.balance)
        else:
            print("please enter correct pin")
    def withdraw(self):
        user_pin= input('enter your pin')
        if user_pin==self.pin:
            amount=input("enter your amount")

            if  amount <= self.balance:
                self.balance= self.balance-amount
                print("withdraw successfull.balanc is",self.balance)
        else:
            print("insufficient balance please enter other amount")
        self.menu()

obj= Atm()

print("obj id :", id(obj))


