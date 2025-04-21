class Bank:

    def __init__(self,balance =10000000):
        self.balance=balance

    def withdraw_balance(self ,amount_to_withdraw):
        amount_to_withdraw=int(input("enter amount"))
        if amount_to_withdraw <= self.balance and amount_to_withdraw >0:
            self.balance=self.balance-amount_to_withdraw
            print(f"Withdrawal successful. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")


bank_account = Bank()  # Creating an account with default balance
amount = int(input("Enter amount to withdraw: "))  # Taking user input
bank_account.withdraw_balance(amount)  # Calling method with user input

#

def missnumber(num):
    miss_number=[]
    for i in range(num[0] , num[-1] +1):
        if i not in num:
            miss_number.append(i)
    return  miss_number

num = [1,3,5,7,9,11]
print(missnumber(num))


def longestsbsecutive(num):
    arr_set=set(num)
    longest_length=0
    word =[]

    for i in range(len(arr_set)):
        if i-1 not in arr_set:
            current_num =i
            current_length=1
            current_word=[current_num]

            while current_num+1 in arr_set:
                current_num+=1
                current_length+=1
                current_word.append(current_num)

            if current_length > longest_length:
                longest_length=current_length
                word=current_word

    return word , longest_length

num=[1,4,6,7,8,9,10]
print(longestsbsecutive(num))

name='my name is    @nitin'
name=[i for i in name if i.isalnum()]
dic={}

for i in name:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

print(dic)
val=[]
for value,count in dic.items():
    if count>1:
        print(value , count)

val =[]
for char in name:
    if dic[char] ==1:
        val.append(char)

print(val)
name1='my name is    @nitin'.split()
rev=[]
for i in range(len(name1)-1 , -1 , -1):
    rev.append(name1[i])
print(rev)


for i in range(1 , len(name1) , 2):
    name1[i] =name1[i] [::-1]
    print(''.join(name1))