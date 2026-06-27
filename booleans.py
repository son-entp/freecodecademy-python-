#== - equal
#!= - not equal
#> - greater than
#< - less than 
#>= - greater than or equal
#<= - less than or equal
#These operators can be used in conditionals to compare values and run certain code based on whether the conditional evaluates to True or False.
#True - 1
#False - 0

age = 18
if age >= 18:
    print('You are an adult')

age = 12
if age >= 18:
    print('You are an adult')#nothing will show up oin terminal

if age >= 18:
    print('You are an adult')
else:
    print('You are not an adult')
#will show up: you are not an adult

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You ar a teenager')
else:
    print("You are a child")


is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')


#and
if is_citizen and age >= 18:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')

#or
age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')

print(not '') # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy

is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')
