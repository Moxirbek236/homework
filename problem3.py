def calculate_painting_time(pattern: list) -> int:
    if not pattern:
        return 0
    
    time = 1 
    time_count = 1
    
    for i in range(1, len(pattern)):
        time += 2 
        if pattern[i] != pattern[i - 1]:
            time_count += 1 
    
    return time + time_count

pattern = ["Green"]
print(calculate_painting_time(pattern))