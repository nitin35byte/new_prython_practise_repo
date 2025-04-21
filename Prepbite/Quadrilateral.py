def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def is_quadrilateral_equal(x1, y1, x2, y2, x3, y3, x4, y4):
    d1 = distance(x1, y1, x2, y2)
    d2 = distance(x2, y2, x3, y3)
    d3 = distance(x3, y3, x4, y4)
    d4 = distance(x4, y4, x1, y1)

    return d1 == d2 == d3 == d4

# Input number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Input coordinates of four points
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    # Check if quadrilateral can be formed with all sides equal
    if is_quadrilateral_equal(x1, y1, x2, y2, x3, y3, x4, y4):
        print("Yes")
    else:
        print("No")
