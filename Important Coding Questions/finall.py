def longestsubsequenciees(arr):
    word=""
    max_length=0
    start=0
    char_fre={}

    for char in range(len(arr)):
        if arr[char] in char_fre and char_fre[arr[char]] >=start:
            start=char_fre[arr[char]]+1

        char_fre[arr[char]]=char

        current_legth= char-start+1
        if current_legth >max_length:
            max_length=current_legth
            word=arr[start:char+1]

    return word  , max_length

arr="bhjabcdefthursz"
print(longestsubsequenciees(arr))