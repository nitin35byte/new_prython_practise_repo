string = "                  geeks quiz practice code"
def rev_sentence(sentence):
   #sentence = input("enter your string: ")
   sentence = "geeks quiz practice code"
   words = sentence.split()
   words.reverse()
   return words

p =rev_sentence(string)
print("first method id:",p)
sentence = "geeks quiz practice code"
if sentence ==sentence[::-1]:
    print(f"{sentence} is reversed")

## second method to reverse the string
string = "geeks quiz practice code"

stack = []
for i in string.split():
    stack.append(i)
    print(i)
print("this is string:",stack)
empty_stack = []
while stack:
    empty_stack.append(stack.pop())
    print(empty_stack)

list=string[::-1]
print("list is:",list)

##test= string.reverse()


for i in string.split():
    print(i)


m = "My name is nitin"
stack = []
for i in m.split():
    stack.append(i)
    print(i)
ss= []
while stack:
    ss.append(stack.pop())
print(ss)


m = "nitin"
stack = []
for i in m.split():
    stack.append(i)
    print(i)
ss= []
while stack:
    ss.append(stack.pop())
print(ss)

if stack==ss:
    print("is palindrome")
else:
    print("Not a palindrome")



word = 'hare krishna hare rama hare krishna hare rama hare krishna hare rama hare krishna hare rama'
stack = []
for i in word.split():
    stack.append(i)

rever = []
while stack:  # Continue while the stack is not empty
    rever.append(stack.pop())

reversed_sentence = ' '.join(rever)  # Join the reversed list into a string
print(reversed_sentence)  # Output: rama hare krishna hare rama hare krishna hare rama hare krishna hare rama hare krishna hare

clean_str=word.strip().split()
left = 0
right =len(clean_str)-1
while left < right:
    clean_str[left], clean_str[right]=clean_str[right],clean_str[left]
    left +=1
    right-=1
reverse_sen= ' '.join(clean_str)
print("reverse string is :",reverse_sen)


def palindrome(l):
    left = 0
    right=len(l)-1

    while left <right:
        if l[left] != l[right]:
            print(f"{l} not a palindrome")
            return  False
        left +=1
        right-=1
    print(f"{l} is a palindrome")
    return True

l = 'rahul'
p = palindrome(l)
print(p)


def reversest(arr):
    arr = arr.split()
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    reverse_sen = ' '.join(arr)
    return reverse_sen

string = "geeks quiz practice code"
a = reversest(string)
print(f"chaged word is :",a)