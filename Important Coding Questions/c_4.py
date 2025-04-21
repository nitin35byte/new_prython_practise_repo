
arr = [64, 34, 25, 12, 22, 11, 90]
is_sorted=True
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        is_sorted=False
        break



if is_sorted:
    print("The table data is sorted.")
else:
    print(f"The table data is not sorted. The unsorted position is at index(1-based index).")


def profit(arr):
    n = len(arr)
    profit=0


    for i in range(0,n):
        if arr[i] > arr[i-1]:
            profit+=arr[i]  - arr[i-1]

    return profit

arr=[5,7,3,8,9]
print(profit(arr))


name= 'my name iS niTiN'

name=name.split()
word=[]
for i in name:
    print(f"name is  -{' '.join(word)}")


from abc import  ABC  ,abstractmethod

class Banking(ABC):

    def login(self):
        print("we are successfull login to the application")

    @abstractmethod
    def security(self):
        print("im security please call me if you want to use banking appliation")


class Banking_user(Banking):

    def person_name(self):
        print("my name is ____")

    def security(self):
        print("security pass")

c=Banking_user()
c.person_name()
c.login()
c.security()


def my_decor(func):


    def wrapper(*args , **kwargs):
        print("we are under wrapper class")

        result=func(*args , **kwargs)

        if isinstance(result , dict):
            return dict(sorted(result.items()))
        print("test define test")

    return wrapper
@my_decor
def est_wrapper():
    print("rapeer is working fine")