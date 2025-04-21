class ATM:
    counter =1
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
        ATM.counter =ATM.counter+ +1

    def menu(self):
        while True:
            print("\nHi, how can I help you?")
            print("1. Press 1 to create pin")
            print("2. Press 2 to change pin")
            print("3. Press 3 to check balance")
            print("4. Press 4 to withdraw")
            print("5. Anything else to exit")

            user_input = input("Please enter your choice: ")

            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.change_pin()
            elif user_input == '3':
                self.check_balance()
            elif user_input == '4':
                self.withdraw()
            else:
                print("Exiting...")
                break

    def create_pin(self):
        self.pin = input('Enter your pin: ')
        self.balance = int(input('Enter your balance: '))
        print("PIN created successfully")
        self.menu()

    def change_pin(self):
        old_pin = input('Enter your old pin: ')
        if old_pin == self.pin:
            new_pin = input("Enter new pin: ")
            self.pin = new_pin
            print("PIN changed successfully")
        else:
            print("Your old pin is incorrect. Please try again later.")
        self.menu()

    def check_balance(self):
        user_pin = input('Enter your pin: ')
        if user_pin == self.pin:
            print('Your balance is', self.balance)
        else:
            print('Please enter correct pin to check balance')

    def withdraw(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            withdraw_amount = int(input("Enter amount to withdraw: "))
            if withdraw_amount <= self.balance and withdraw_amount > 0:
                self.balance -= withdraw_amount
                print("Please collect your cash. Your balance is now", self.balance)
            else:
                print('Please enter a valid amount')
        else:
            print("Please enter valid pin")
        self.menu()

# Example usage
atm = ATM()
