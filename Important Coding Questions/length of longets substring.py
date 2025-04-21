def longestsubstring(s):
    char_index={}
    max_length=0
    start=0
    substring = ""
    for char in range(len(s)):
        if s[char] in char_index:
            start=max(start , char_index[s[char]]+1)
        char_index[s[char]] = char

        current_length = char - start + 1
        if current_length > max_length:
            max_length = current_length
            substring = s[start:char + 1]

        max_length=max(max_length , char-start+1)
    return  max_length  ,substring

arr='abcdabcdefabcdef'
print(longestsubstring(arr))



def longestsubstring(s):
    char_index = {}
    max_length = 0
    start = 0
    substring = ""

    for char in range(len(s)):
        if s[char] in char_index and char_index[s[char]] >= start:
            start = char_index[s[char]] + 1
        char_index[s[char]] = char

        current_length = char - start + 1
        if current_length > max_length:
            max_length = current_length
            substring = s[start:char + 1]

    return max_length, substring

arr = 'bhjabcdefthur'
length, substring = longestsubstring(arr)
print("Longest Substring Length:", length)
print("Longest Substring:", substring)


def longestsubstring(s):
    max_length = 0
    word = ""
    start = 0
    char_frequency = {}

    for i in range(len(s)):
        if s[i] in char_frequency and char_frequency[s[i]] >= start:
            start = char_frequency[s[i]] + 1
        char_frequency[s[i]] = i

        current_max = i - start + 1
        if current_max > max_length:
            max_length = current_max
            word = s[start:i + 1]
    return max_length, word


#arr = 'abcdabcdefabcdef'
arr="bhgijfsdethe"
max_length, word = longestsubstring(arr)
print("Longest Substring Length:", max_length)
print("Longest Substring:", word)

def common_prefix(arr):
    min_str=min(arr)
    max_arr=max(arr)
    common=""

    len_of_min_str=len(min_str)

    for i in range(len_of_min_str):
        if min_str[i] == max_arr[i]:
            common+=min_str[i]

    return common

arr=["flt","fly","fle"]
print(common_prefix(arr))