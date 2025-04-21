def nested_list_sum(lst):
    total=0
    for item in lst:
        if isinstance(item,list):
            total+=nested_list_sum(item)
        else:
            total +=item
    return total

nested_list=[-1,[2 , 4],[3 ,4 ,5]]
result=nested_list_sum(nested_list)
print(result)


def nested_sum(lst):

    total = 0
    for i in lst:
        if type(i) == list:
            total+= nested_sum(i)
        else:
            total +=i
    return total

nested_list=[-7,[2 , 4],[3 ,4 ,5]]
result=nested_sum(nested_list)
print(result)

def nested_sum(lst):

    total = []
    for i in lst:
        if type(i) == list:
            total.extend(nested_sum(i))
        else:
            total.append(i)
    return total

nested_list=[-7,[2 , 4],[3 ,4 ,5]]
result=nested_sum(nested_list)
print(result)