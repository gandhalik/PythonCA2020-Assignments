def double_list(n):
    return n * n


li = [1, 2, 3, 4]
result = map(double_list, li)
print(list(result))