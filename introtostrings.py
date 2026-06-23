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