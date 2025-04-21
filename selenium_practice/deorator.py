def my_function(func):

    def wrapper(*args):
        print("calculation sum")
        result =func(*args)
        print("calculation done")
        return result
    return wrapper


@my_function
def sum2(a , b , d):
    c=a+b +d
    print(c)

a=sum2(3 ,4 , 5)
