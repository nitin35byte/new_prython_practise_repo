def max_min(arr):
    l = len(arr)
    max_val = arr[0]
    min_val = arr[0]

    for i in range( l):
        if arr[i] > max_val:
            max_val = arr[i]

        elif arr[i] < min_val:
            min_val = arr[i]

    return max_val, min_val

# Example usage:
arr = [3, 5, 2, 8, 1]
max_val, min_val = max_min(arr)
print("Maximum value:", max_val)
print("Minimum value:", min_val)

arr = [3, 5, 2, 8, 100]
l = arr[0]
b = arr[0]

for i in arr:
    if i >l:
        l =i
    if i <b:
            b = i

print(l,b)



