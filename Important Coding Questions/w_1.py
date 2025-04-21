class Banking:

    def __init__(self,bank_name , ifsc_code):
        self.bank_name=bank_name
        self.ifsc_code=ifsc_code


    def customer_name(self , customerName , customer_number):
        self.__customerName=customerName
        self.__customer_number=customer_number


    def __str__(self):
        return f"my name is {self.__customerName} and my phonenumber is{self.__customer_number}"

    def get_name(self):
        return self.__customer_number


    def get_number(self):
        return self.__customer_number

    def update_number(self,new_number):

        if len(str(new_number)) ==10 and isinstance(new_number , int):
            self.__customer_number=new_number
        return new_number


B=Banking("hdfc" ,"HDFC0023")
print(B.ifsc_code)
print(B.bank_name)
B.customer_name("nitin" , 98322222)
print(B)
B.update_number(123133333)
print(B.update_number(432456))

def test_p():
    assert