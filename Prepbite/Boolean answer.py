def max_completed_cow(rows):
    max_completed = -1
    max_row_index =-1

    for i  ,row in enumerate(rows):
        completed_count=sum(row)
        if completed_count >max_completed:
            max_completed=completed_count
            max_row_index=i+1

    return max_row_index if max_completed>0 else -1
