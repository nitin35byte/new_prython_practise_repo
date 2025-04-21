def reverse_string_with_spaces(input_str):
    # Convert the input string into a list of characters
    char_list = list(input_str)

    # Initialize variables for constructing the reversed string
    reversed_str = [''] * len(char_list)
    end = len(char_list) - 1

    # Traverse the input string from right to left
    for i in range(len(char_list)):
        # Skip over spaces by leaving the current position unchanged
        if char_list[i] == ' ':
            continue

        # Find the next space to determine word boundaries
        while end >= 0 and char_list[end] == ' ':
            end -= 1

        # Copy non-space characters to the reversed string
        reversed_str[end] = char_list[i]
        end -= 1

    # Join the list of characters into a single string
    reversed_output = ''.join(reversed_str)

    return reversed_output


# Test the function
input_str = 'My name is nitin'
result = reverse_string_with_spaces(input_str)
print(result)
