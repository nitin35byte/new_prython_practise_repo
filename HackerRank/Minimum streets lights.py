

def Sort_Tuple(tup):
    lst = len(tup)
    for i in range(lst):
        for j in range(lst - i - 1):
            if tup[j][1] > tup[j + 1][1]:
                tup[j], tup[j + 1] = tup[j + 1], tup[j]

    return tup

def solve(l, n):
    rang = [[0, 0] for _ in range(n)]
    for i in range(n):
        id = i + 1
        rang[i][0] = max(i, id - l[i])
        rang[i][1] = min(i, id + l[i])

    sorted_rang = Sort_Tuple(rang)

    max_range = 0
    current_range_end = 0
    for i in range(n):
        if sorted_rang[i][0] > current_range_end:
            max_range += sorted_rang[i][0] - current_range_end
            current_range_end = sorted_rang[i][1]

    max_range += n - current_range_end

    return max_range

# Main part
n = int(input("Enter the number of elements in the list: "))
l = []
for i in range(n):
    l.append(int(input(f"Enter the value for element {i + 1}: ")))

print("Maximum range:", solve(l, n))


def test():
    print("executed first")
@test
def test1(*args):
    c =a +b
    return c
