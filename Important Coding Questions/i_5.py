def consecutive_number(arr):
    ar_set=set(arr)
    max_length=0
    word=[]

    for num in ar_set:
        if num-1 not in ar_set:
            current_num=num
            current_max=1
            current_word=[current_num]

            while current_num+1 in ar_set:
                current_num+=1
                current_max+=1
                current_word.append(current_num)

            if current_max >max_length:
                max_length=current_max
                word =current_word
            max_length=max(max_length , current_max)
    return max_length , word


arr=[1 , 55 , 2, 7 , 99 , 3 , 5 , 4]
print(consecutive_number(arr))

def commprefix(word):
    max_word=max(word)
    min_word=min(word)
    comm=''

    len_min_word=len(min_word)

    for i in range(len_min_word):
        if min_word[i] == max_word[i]:
            comm+=min_word[i]
        else:
            break

    return comm

word = ['fly' , 'flytr' , 'flytw']
print(commprefix(word))



def longestsubstring(arr):

    max_lenghth=0
    start=0
    word=''
    #word=set()
    frequency={}

    for i in range(len(arr)):
        if arr[i] in frequency and frequency[arr[i]] >= start:
            start = frequency[arr[i]]
        frequency[arr[i]]= i

        current__max= i- start +1
        if current__max >max_lenghth:
            max_lenghth =current__max
            word = arr[start :i+1]
    return word ,max_lenghth


arr='abcrfabcdefgfghy'
b = longestsubstring(arr)
print(f"longest substring is {b}")



def misssing_number(arr):
    miss =[]
    for i in range(len(arr) , arr[-1] +1):
        if i not in arr:
            miss.append(i)
    return  miss
a = [1, 2, 3, 4, 6, 8, 10]
missing_elements = misssing_number(a)
print("Missing elements:", missing_elements)
