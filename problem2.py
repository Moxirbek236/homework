def find_top_three_numbers_sorted(data: list) -> list:
    result = []
    
    for numbers in data:
        unique_numbers = sorted(numbers, reverse=True)
        top_three = unique_numbers[:3]
        result.append(tuple(top_three))
    
    return result

data = [(10, 20, 30, 11), (5, 15), (40,), (7, 8, 50, 3)]
print(find_top_three_numbers_sorted(data))  