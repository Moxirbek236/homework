def merge_unique_ids(active_users: list, new_users: list) -> list:
    unique_ids = []
    
    for user_id in active_users + new_users:
        if user_id not in unique_ids:
            unique_ids.append(user_id)
    
    return unique_ids

active_users = ['U1001', 'U1002', 'U1003', 'U1004', 'U1001']
new_users = ['U1003', 'U1005', 'U1006', 'U1002', 'U1007']
print(merge_unique_ids(active_users, new_users))
