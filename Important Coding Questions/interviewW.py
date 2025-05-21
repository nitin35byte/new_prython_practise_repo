data = [("kohli", 8, 500), ("rahul", 8, 600), ("pooran", 8, 500), ("rohit", 8, 400), ("salt", 8, 800)]

def average(data):
    total = 0
    matched = 0
    for name, match, run in data:
        total += run
        matched += match
    return total / matched

overall_avg = average(data)

# Find the first batsman with average > overall average
for name, match, run in data:
    player_avg = run / match
    if player_avg > overall_avg:
        print(f"Batsman: {name}, Average: {player_avg:.2f} (Above overall average {overall_avg:.2f})")
        break
