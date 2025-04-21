def removeduplicate(input_list):
    seen =set()

    return [x for x in input_list if not(x in seen or seen.add(x))]
input_list = [1, 2, 2, 3, 4, 1, 5, 3]
obj =removeduplicate(input_list)


print(obj)



def remove_duplicates(input_list):
    seen = set()

    for x in input_list:
        if x not in seen:
            seen.add(x)
            yield x

input_list = [1, 2, 2, 3, 4, 1, 5, 3]
result = list(remove_duplicates(input_list))
print(result)  # Output: [1, 2, 3, 4, 5]