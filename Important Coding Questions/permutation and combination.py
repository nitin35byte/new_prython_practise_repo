def get_permutations(s, step=0):
    if step == len(s):
        print("".join(s))  # Print each permutation
    for i in range(step, len(s)):
        s_copy = [char for char in s]  # Create a copy of the string as a list
        s_copy[step], s_copy[i] = s_copy[i], s_copy[step]  # Swap
        get_permutations(s_copy, step + 1)

word = "rahul"
get_permutations(list(word))  # Convert to list since strings are immutable

def happy_holi(date):
    if date==2:
        print("happy holi")
    else:
        print("wait kar le holi ki")
date=28
print(happy_holi(date))