def longest_common_sub(test1 , text2):
    m , n=len(test1) , len(text2)

    dp=[[0] *(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if test1[i-1]==text2[j-1]:
                dp[i][j] =1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j] , dp[i][j-1])

    return dp[m][n]

text1 = "abcde"
text2 = "ace"
print("Length of LCS:", longest_common_sub(text1, text2))


def common_prefix(arr):

    min_arr=min(arr)
    max_arr=max(arr)
    commpre=""
    len_min_arr=len(min_arr)

    for i in range(len_min_arr):
        if min_arr[i]==max_arr[i]:
            commpre+=min_arr[i]
        else:
            break

    return commpre

arr=['fly','flyuid','flyreee']
print(common_prefix(arr))


def dp_probem(text1,text2):
    m , n=len(text1) , len(text2)

    dp=[[0] * (m+1) for _ in range(n+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j]  , dp[j-1][i])



    return dp[m][n]

text1 = "abcde"
text2 = "ace"
print("Length of LCS:", longest_common_sub(text1, text2))


def longes_scustestring(arr):
    arr_set=set(arr)

    max_length=0
    word=[]

    for i in arr_set:
        if i-1 not in arr_set:
            current_num=i
            current_lenghth=1
            current_streak=[current_num]

            while current_num+1 in arr_set:
                current_num+=1
                current_lenghth+=1
                current_streak.append(current_num)

            if current_lenghth > max_length:
                max_length=current_lenghth
                word=current_streak

    return max_length , word

arr=[1,2,6,77,3,4,5,66,7,8,9]
print(longes_scustestring(arr))

def longestsubstring(arr):

    char_fre={}
    max_length=0
    word=''
    start=0

    for i in range(len(arr)):
        if arr[i] in char_fre and char_fre[arr[i]] >= start:
            start = char_fre[arr[i]]+1

        char_fre[arr[i]]=i

        currennt_max=i-start+1
        if currennt_max > max_length:
            max_length=currennt_max
            word=arr[start:i+1]

    return max_length,word

arr='abcdedbfghtukw'
print(longestsubstring(arr))


def reverse_in_subsets(arr, n):
    for i in range(0 , len(arr) , n):
        arr[i:i+n] = reversed(arr[i:i+n])

        return arr

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
subset_size = 3
result = reverse_in_subsets(array, subset_size)
print(result)


def first_negative_in_window(arr, n):
    result = []

    for i in range(len(arr)-n+1):
        window=arr[i:i+n]

        for num in window:
            if num > 0:
                result.append(num)
                found=True
                break
        if not found:
            result.append(0)

    return result

# Example usage
array = [12, -1, -7, 8, -15, 30, 16, 28]
window_size = 3
output = first_negative_in_window(array, window_size)
print(output)

def reverse_alternate_words(input_string):
    words = input_string.split()
    for i in range(1, len(words) , 2):
        words[i]=words[i][::-1]
    return words

input_string = "selenium playwright robot webdriver"
output = reverse_alternate_words(input_string)
print(output)


def miss_number(arr):
    miss_nu=[]
    for i in range(arr[0], arr[-1]+1):
        if i not in arr:
            miss_nu.append(i)
    return miss_nu

arr=[1,3,5,7,9,11]
print(miss_number(arr))