def perfect_square(num):
    if num <0:
        return False
    if num == 0:
        return True

    left , right = 1 , num
    while left <= right:
        mid = (left + right)//2
        square = mid*mid

        if square == num:
            return True
        if square<num:
            left = mid +1
        else:
            right = mid-1

    return False

    # Example usage
print(perfect_square(16))  # Output: True (4*4 = 16)
print(perfect_square(49))  # Output: False