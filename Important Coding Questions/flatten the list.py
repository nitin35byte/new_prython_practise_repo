def flattern_list(l):
    flat_list=[]
    total=0
    for i in l:
        if isinstance(i , list):
            sub_list, sub_total = flattern_list(i)
            flat_list.extend(sub_list)
            total+=sub_total
        else:
            flat_list.append(i)
            total+=i
    return flat_list  , total

l=[1,2,3,[4,5],6,[7,8],9]
print(flattern_list(l))


