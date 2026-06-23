my_str = 'Hello world'

print('Hello' in my_str) #True
print('Hell' in my_str) #True
print('hey' in my_str) #False
print('f' in my_str)

print(len(my_str))

print(my_str[0]) #H
print(my_str[6]) #w
print(my_str[-1]) #d
print(my_str[-2]) #l

name = "Artsiom"
surname = 'Zahzhetski'
full_name = name + ' ' + surname
print(full_name) #Artsiom Zahzhetski
#BUTTT. WE CAN'T PLUS NOT THE SAME TYPE OF VARIABLES

#age = 15
#full_name += str(age)
#print(full_name) #Artsiom Zahzhetski15

oone = f'My name is {name} and my surname is {surname}. In passport - {full_name}'
print(oone)

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15

#string[start:stop]
print(my_str[1:5])
print(my_str[:8])
print(my_str[5:])

#string[start:stop:step]
print(my_str[1:11:2])
print(my_str[::-1])

uppercasemystr = my_str.upper
lowercasemystr = my_str.lower
print(uppercasemystr)
print(lowercasemystr)

my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # "hello world"

my_str = 'hello world'
replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world

split_words = my_str.split()
print(split_words)  # ['hello', 'world']

my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True
ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True
world_index = my_str.find('world')
print(world_index)  # 6
o_count = my_str.count('o')
print(o_count)  # 2
capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world
is_all_upper = my_str.isupper()
print(is_all_upper)  # False
is_all_lower = my_str.islower()
print(is_all_lower)  # True
title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World

