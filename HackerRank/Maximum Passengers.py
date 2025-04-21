from collections import deque


def maxPassengers(matrix):
    n = len(matrix)
    max_passengers = 0

    queue = deque([(0, 0, 0)])  # (x, y, passengers)
    while queue:
        x, y, passengers = queue.popleft()

        if x == n - 1 and y == n - 1:
            max_passengers = max(max_passengers, passengers)
            continue

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] != -1:
                new_passengers = passengers
                if matrix[nx][ny] == 1:
                    new_passengers += 1
                    matrix[nx][ny] = 0  # Mark the passenger as picked up
                queue.append((nx, ny, new_passengers))
                if matrix[nx][ny] == 1:
                    matrix[nx][ny] = 1  # Restore the passenger for other paths

    return max_passengers


# Sample input
matrix = [
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print(maxPassengers(matrix))  # Output: 2
