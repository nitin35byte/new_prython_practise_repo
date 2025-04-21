def unique_colors(N , colors):
    unique_set = set()


    for color in colors:
        unique_set.add(color)

    return len(unique_set)

N = int(input())

color = list(map(int , input().split()))

M = unique_colors(N, color)

# Print the result
print(M)