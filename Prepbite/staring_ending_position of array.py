def find_positions(arr, target):
    start_pos = -1
    end_pos = -1

    for i in range(len(arr)):
        if arr[i] == target:
            if start_pos == -1:
                start_pos = i
            end_pos = i

    return start_pos, end_pos

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
start, end = find_positions(arr, target)
if start == -1:
    print("Element not found in array")
else:
    print("Starting position:", start)
    print("Ending position:", end)
