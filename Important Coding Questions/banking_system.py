import logging
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def add_account(self, account):
        if account.number not in self.accounts:
            self.accounts[account.number] = account
            logging.info(f"Account {account.number} created successfully.")
        else:
            logging.warning(f"Account {account.number} already exists.")

    def get_account(self, number):
        return self.accounts.get(number)

    def remove_account(self, number):
        if number in self.accounts:
            del self.accounts[number]
            logging.info(f"Account {number} removed successfully.")
        else:
            logging.warning(f"Account {number} not found.")

class Account:
    def __init__(self, number, owner, balance):
        self.number = number
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction(amount, 'Deposit'))
            logging.info(f"Deposit of {amount} successful.")
        else:
            logging.error("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transactions.append(Transaction(amount, 'Withdrawal'))
                logging.info(f"Withdrawal of {amount} successful.")
            else:
                logging.error("Insufficient funds.")
        else:
            logging.error("Invalid withdrawal amount.")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions

class Transaction:
    def __init__(self, amount, type):
        self.amount = amount
        self.type = type

def main():
    logging.info('Bank Management System started.')

    bank_name = input('Enter bank name: ')
    bank = Bank(bank_name)
    logging.info(f'{bank_name} Bank Management System initialized.')

    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. View Transactions")
        print("6. Remove Account")
        print("7. Exit")
        choice = input('Enter your choice: ')

        try:
            if choice == '1':
                acc_number = input('Enter account number: ')
                if not acc_number.isdigit() or len(acc_number) != 10:
                    print("Invalid account number. Please enter a 10-digit numeric account number.")
                    continue  # Skip account creation and go back to the main menu
                acc_owner = input('Enter account owner name: ')
                acc_balance = float(input('Enter opening balance: '))
                account = Account(acc_number, acc_owner, acc_balance)
                bank.add_account(account)

            elif choice == '2':
                acc_number = input('Enter account number: ')
                amount = float(input('Enter amount to deposit: '))
                if amount <= 0:
                    print("Invalid amount. Please enter a positive number.")
                    continue  # Skip deposit and go back to the main menu
                account = bank.get_account(acc_number)
                if account:
                    account.deposit(amount)
                else:
                    raise ValueError("Account not found.")


            elif choice == '3':
                acc_number = input('Enter account number: ')
                amount = float(input('Enter amount to withdraw: '))
                account = bank.get_account(acc_number)
                if account:
                    account.withdraw(amount)
                else:
                    raise ValueError("Account not found.")

            elif choice == '4':
                acc_number = input('Enter account number: ')
                account = bank.get_account(acc_number)
                if account:
                    print(f"Balance of account {acc_number}: {account.get_balance()}")
                else:
                    raise ValueError("Account not found.")

            elif choice == '5':
                acc_number = input('Enter account number: ')
                account = bank.get_account(acc_number)
                if account:
                    transactions = account.get_transactions()
                    print(f"Transactions of account {acc_number}:")
                    for transaction in transactions:
                        print(f"{transaction.type}: {transaction.amount}")
                else:
                    raise ValueError("Account not found.")

            elif choice == '6':
                acc_number = input('Enter account number: ')
                bank.remove_account(acc_number)

            elif choice == '7':
                print('Thank you for using the Bank Management System.')
                break

            else:
                logging.error('Invalid choice. Please try again.')
        except ValueError as e:
            logging.error(f"Error: {e}")

if __name__ == '__main__':
    main()
