my_list = ['apple', 'banana', 'cherry']
dict_from_list = {index: value for index, value in enumerate(my_list)}
print(dict_from_list)
my_list = ['banana', 'cherry','apple']
b = [1,2,3]
dd=dict(zip( b,my_list))
print(dd)
re=sorted(dd.items(),key=lambda x:x[0])
print(re)


def sort_dictionary(func):
    def wrapper(*args , **kwargs):

        result=func(*args , **kwargs)

        if isinstance(result , dict):
            return dict(sorted(result.items()))
        return result
    return wrapper


@sort_dictionary
def convert_and_sort_list_to_dict(my_list):
    # Convert list to dictionary with default value 0
    return dict.fromkeys(my_list, 0)

my_list = ['apple', 'banana', 'cherry']
sorted_dict = convert_and_sort_list_to_dict(my_list)

print("Sorted Dictionary by Keys:", sorted_dict)


a=[1,2,3,4,5]
b=[2,9,4,6,8]
a.extend(b)
print(a)
c=[98,99,100]
a.append(c)
print(a)

# def c_test():
#     print("pass")
#
# class Gaurav:
#
#     def gaurav_occupation(self , occupation):
#         self.occupation=occupation


a=[10,10]
b=[a,b]
r=dict(zip(a,b))
print(r)

class ATM:
    def __init__(self):
        self.pin="1234"
    def create_poin(self):
        old_pin=input("enter old pin")
        if self.pin==old_pin:
            new_pin=input("enter new pin")
            if new_pin.isdigit() and len(new_pin)==4:
                self.pin=new_pin
                print("PIN changed successfully!")
            else:
                print("Invalid PIN! It must be a 4-digit number.")

        else:
            print("Incorrect old PIN!")

atm=ATM()
atm.create_poin()

class Encp:
    def __init__(self , balance , account_number):
        self.__balance=balance
        self.__account_number=account_number

    def get_balance(self):
        return self.__balance

    def get_accountNumber(self):
        return self.__account_number()


    def update_balance(self , new_balance):

        new_balance=int(input("entr new balance"))
        if isinstance(new_balance  , int) and new_balance >0:
            self.__balance=new_balance

        return new_balance


e=Encp(1234 , 7690654341551)
print(e.get_balance())
e.update_balance(7000)  # Updating balance
print("Updated Balance:", e.get_balance())
