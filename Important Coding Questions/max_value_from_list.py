def find_max_element(lst):
    f1 = lst[0]
    for i in lst:
        if i > f1:
            f1 = i
    return f1

# Test the function
lst = [10, 5, 20, 8, 15]
max_num = find_max_element(lst)
print("Maximum element in the list:", max_num)



## max 2 value from list

lst = [10, 5, 20, 8, 19]
f1 = lst[0]
f2 = lst[0]

for i in lst:
    if i > f1:
        f2 = f1
        f1 = i
    elif i > f2:
        f2 = i

print("Largest element:", f1)
print("Second largest element:", f2)


l = [3, 4, 5, 7, 1, 8, 9,11]

smallest = l[0]
largest = l[0]

for i in l:
    if i > largest:
        largest = i

    elif i < largest:
        smallest = i

print("Smallest and largest numbers are:", smallest, largest)
l = [3, 4, 5, 7, 1, 8, 9,11]
MAX_value=l[0]
second_max =l[0]
for  i in l:
    if i > MAX_value:
        second_max = MAX_value
        MAX_value=i
    elif i> second_max:
        second_max=i

print("second max value in list is:",second_max)


##find samlles and second smalles
smallest_value=l[0]
second_smalles=l[0]
for i in l:
    if i < smallest_value:
        second_smalles=smallest_value
        smallest_value=i

    elif  i <second_smalles:
       # smallest_value=second_smalles
        second_smalles = i

print("smallest and second smallest value:", smallest_value, second_smalles)



arr = [5, 7, 4, 3, 9, 8, 19, 21]

maximum = float('-inf')  # Initialize maximum with negative infinity
second_maximum = float('-inf')  # Initialize second maximum with negative infinity
lowest = float('inf')  # Initialize lowest with positive infinity

for num in arr:
    if num > maximum:
        second_maximum = maximum
        maximum = num
    elif num > second_maximum and num < maximum:
        second_maximum = num

    if num < lowest:
        lowest = num

print("Maximum:", maximum)
print("Second Maximum:", second_maximum)
print("Lowest:", lowest)
