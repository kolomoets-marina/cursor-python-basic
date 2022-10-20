int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

# 1. Define the id of next variables:
print(id(int_a))
print(id(str_b ))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.extend([4,5])
print(id(lst_d))

# 3. Define the type of each object from step 1.
print(type(int_a))
print(type(str_b ))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

# 4*. Check the type of the objects by using isinstance.
print(isinstance(int_a,int))
print(isinstance(str_b,str ))
print(isinstance(set_c,set))
print(isinstance(lst_d,list))
print(isinstance(dict_e,dict))

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

# 5. With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(5, 9))

# 6. By passing index numbers into the curly braces.
print("Anna has {1} apples and {0} peaches.".format(9, 5))

# 7. By using keyword arguments into the curly braces.
print("Anna has {apple} apples and {peache} peaches.".format(apple=5, peache=9))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {apple:5} apples and {peache:3} peaches.".format(apple=5, peache=9))

# 9. With f-strings and variables
apple = 5
peache = 9

print(f"Anna has {apple} apples and {peache} peaches.")

# 10. With % operator
print("Anna has %s apples and %s peaches." % (apple, peache))

# 11*. With variable substitutions by name (hint: by using dict)
frut_dict = { "appl": 20, "peac": 10 }

print("Anna has {} apples and {} peaches.".format(frut_dict["appl"],frut_dict["peac"]))

#12. Convert (1) to list comprehension
list_comprehension_1 = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comprehension_1)

#13. Convert (2) to regular for with if-else
lst1 = []
for num in range(10):
    if num % 2 == 0:
        lst1.append(num // 2)
    else:
        lst1.append(num * 10)
print(lst1)

#14. Convert (3) to dict comprehension.
dict_comprehension = {num: num**2 for num in range(1, 11) if num % 2 == 1}
print(dict_comprehension)

#15*. Convert (4) to dict comprehension.
dict_comprehension = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict_comprehension)

#16. Convert (5) to regular for with if.
d = {}
for x in range(10):
    if x**3 % 4 == 0:
        d[x] = x**3
print(d)

#17*. Convert (6) to regular for with if-else.
d = {}
for x in range(10):
    if x**3 % 4 == 0:
        d[x] = x**3
    else:
        d[x] = x
print(d)

#18. Convert (7) to lambda function
foo = lambda x, y: x if x < y else x

#19*. Convert (8) to regular function
def foo(x, y, z):
    if x < y and x > z:
        return z
    else:
        return y

#20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))

#21. Sort lst_to_sort from max to min
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort, reverse=True))

#22. Use map and lambda to update the lst_to_sort by multiply each element by 2
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_lmb = list(map(lambda x: x*2, lst_to_sort))
print(lst_lmb)

#23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]

lst_lmb = list(map(lambda x, y: x**y, list_A, list_B))
print(lst_lmb)

#24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
filtered = list(filter(lambda x: x % 2 == 1, lst_to_sort))
print(filtered)

#25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
b = range(-10, 10)
filtered_2 = list(filter(lambda x: x < 0, b))
print(filtered_2)

#26*. Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
common = list(filter(lambda n: n in list_1, list_2))
print(common)
