def foo(value, lst):
    value = 1
    lst[0] = 44

v = 3
lst = [1, 2, 3]
foo(v, lst)
print(v, lst[0])