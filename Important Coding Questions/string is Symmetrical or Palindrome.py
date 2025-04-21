def is_palindrome(name: str) -> bool:
    name = name.lower()
    stack = []

    # Push all characters of the string onto the stack
    for char in name:
        stack.append(char)

    # Pop characters from the stack to form the reversed string
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()

    # Check if the original string is equal to the reversed string
    return name == reversed_string

# Example usage
name = 'Nitin'
if is_palindrome(name):
    print(f"{name} is a palindrome")
else:
    print(f"{name} is not a palindrome")


name = 'ANjali'
name= name.lower()

left=0
right= len(name)-1
while left <right:
	if name[left] != name[right]:
		is_palindrome=False
		break
	left +=1
	right -=1
if is_palindrome:
    print(f"{name} is a palindrome")
else:
    print(f"{name} is not a palindrome")


protiviti = 'madam'

if protiviti== protiviti[::-1]:
	print(f"{protiviti} is palindrome")
else:
    print(f"{protiviti} is not a palindrome")




name = "My name is nitin"
name= name.split()

stack = []
for i in name:
    stack.append(name)
rever=[]
while stack:
    rever.append(stack.pop())
reversre_sec = " ".join(rever)
print(reversre_sec)