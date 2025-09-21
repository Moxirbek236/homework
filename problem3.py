def calculate_painting_time(pattern: list) -> int:
    if not pattern:
        return 0
    
    time = 1  # Start with 1 minute for the first section
    time_count = 1
    
    for i in range(1, len(pattern)):
        time += 2  # Increment time if the color changes
        if pattern[i] != pattern[i - 1]:
            time_count += 1  # Reset time count for a new color
    
    return time + time_count

pattern = ["Green"]
print(calculate_painting_time(pattern))