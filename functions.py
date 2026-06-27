name = input('What is your name?') # User types "Kolade" and presses Enter  
print('Hello', name) # Output: Hello Kolade

def hello():
    print('Hello world!')
hello()

def calc_sum(a, b):
    print(a + b)
calc_sum(12, 7)

def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(3, 1)
print(my_sum) # 4

def my_func():
    my_var = 10 # Locally scoped to my_func
    print(my_var)

my_func() # 10

#print(my_var) # NameError: name 'my_var' is not defined
