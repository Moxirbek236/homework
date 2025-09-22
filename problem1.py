def merge_unique_ids(active_users: list, new_users: list) -> list:
    unique_ids = set(user_id for user_id in active_users + new_users if user_id in active_users + new_users)
    unique_ids = list(sorted(unique_ids))
    return unique_ids

active_users = ['U1001', 'U1002', 'U1003', 'U1004', 'U1001']
new_users = ['U1003', 'U1005', 'U1006', 'U1002', 'U1007']
print(merge_unique_ids(active_users, new_users))