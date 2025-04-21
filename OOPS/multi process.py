import multiprocessing

import time

def print_number():
    for i in range(5):
        time.sleep(1)
        print(i)

def print_word():
    for letter in 'abcde':
        time.sleep(1.5)
        print(letter)

thread1=multiprocessing.Process(target=print_number())
thread2=multiprocessing.Process(target=print_word())

thread1.start()
thread2.start()

thread1.join()
thread2.join()