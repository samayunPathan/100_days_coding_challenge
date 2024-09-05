def find_big(n):
    max_val = 0
    while n > 0:
        r = n % 10
        max_val = max(max_val, r)
        n = n//10
    return max_val


print(find_big(1287029))
