def my_decorator(func):

    def wraper():
        print("i m under wrapper")

        func()

        print("out of func function")
    return wraper

@my_decorator
def summ():

    print("test data")

summ()