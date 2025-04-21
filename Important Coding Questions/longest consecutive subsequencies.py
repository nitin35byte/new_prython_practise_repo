def longestconsecutive(num):
    longest_strak=0
    arr_set=set(num)
    arr=[]

    for num in arr_set:
        if num -1 not in arr_set:
            current_num = num
            current_streak=1
            current_sequence=[current_num]

            while current_num+1 in arr_set:
                current_num +=1
                current_streak +=1
                current_sequence.append(current_num)

            if current_streak > longest_strak:
                longest_strak=current_streak
                arr=current_sequence

            longest_strak=max(longest_strak , current_streak)
    return longest_strak , arr


arr=[1, 2 ,7 , 8 , 44 , 1  ,2 , 5 ,3 ,4 , 7, 6]
s= longestconsecutive(arr)
print(s)



# def lcs(arr):
#     curr_arr=set(arr)
#     word=[]
#     longest_streak=0
#
#     for num in curr_arr:
#         if num-1 not in curr_arr:
#             current_num =num
#             current_sreak=1
#             current_sequence=[current_num]
#
#             while num +1 in curr_arr:
#                 current_num+=1
#                 current_sreak +=1
#                 current_sequence.append(current_num)
#
#             if current_sreak > longest_ streak:
#                 longest_streak=current_sreak
#                 word=current_sequence
#
#             longest_streak=max(longest_streak , current_num)
#
#     return word , longest_streak
#
# arr=[1, 2 ,7 , 8 , 44 , 1  ,2 , 5 ,3 ,4 , 7, 6]
# s= lcs(arr)
# print(s)
