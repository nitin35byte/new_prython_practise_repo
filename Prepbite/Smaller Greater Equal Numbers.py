def count_baskets(N, K, baskets):
    L = M = E = 0
    for factor in baskets:
        if factor < K:
            L += 1
        elif factor > K:
            M += 1
        else:
            E += 1
    return L, M, E

# Input number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Input N and K
    N, K = map(int, input().split())

    # Input quality factors of the baskets
    baskets = list(map(int, input().split()))

    # Count baskets with quality factors less than, equal to, and more than K
    L, M, E = count_baskets(N, K, baskets)

    # Print the results
    print(L, M, E)
