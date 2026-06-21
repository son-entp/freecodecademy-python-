age = 15 #py knows, that this is int
name = "Artsiom" #py knows, that this is str
surname = "Zahzhetski"

li_lilo_li_pop99 = ("idk")

print("Hello world") #hello world
print('Hello', 'world')
print('My fav colors are', 'green', 'white', 'navy blue', 'and', 'purple')#they will be separated automaticly

my_integer_var = 10
print('Integer:', my_integer_var) # Integer: 10
#Integer - a whole number without decimals

my_float_var = 4.50
print('Float:', my_float_var) # Float: 4.5
#Float - a number with a decimal point. like: 4.4, 4.005 ....

my_string_var = 'hello'
print('String:', my_string_var) # String: hello
#String: A sequence of characters enclosed in single or double quotation marks like 'Hello world!'.

my_boolean_var = True
print('Boolean:', my_boolean_var) # Boolean: True
#Boolean - a true or false type

my_set_var = {7, 'hello', 8.5}
print('Set:', my_set_var) # Set: {7, 'hello', 8.5}
#set - an unordered collection of unique elements(it can be a float, an int, a string or a boolean)

my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', my_dictionary_var) # Dictionary: {'name': 'Alice', 'age': 25}
#Dictionary - a collection of key-value pairs

my_tuple_var = (7, 'hello', 8.5)
print('Tuple:', my_tuple_var) # Tuple: (7, 'hello', 8.5)
#truple - An immutable ordered collection, enclosed in parentheses

my_range_var = range(5)
print('Range:', my_range_var) # Range: range(0, 5)
# Range with one argument (stop only)
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4

# Range with start and stop
for i in range(2, 7):
    print(i, end=" ")  # 2 3 4 5 6

# Range with start, stop, and step
for i in range(1, 10, 2):
    print(i, end=" ")  # 1 3 5 7 9

# Counting backwards
for i in range(10, 0, -2):
    print(i, end=" ")  # 10 8 6 4 2

my_list = [22, 'Hello world', 3.14, True]
print(my_list) # [22, 'Hello world', 3.14, True]
#List: An ordered collection of elements that supports different data types.

my_none_var = None
print('None:', my_none_var) # None: None
#None: A special value that represents the absence of a value.

