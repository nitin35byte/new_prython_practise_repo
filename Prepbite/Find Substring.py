def is_substring(s,t):
    if t in s:
        return "Yes"
    else:
        return "No"

T = int(input())

for _ in range(T):
    s,t = input().split()

    result = is_substring(s,t)

    print(result)
