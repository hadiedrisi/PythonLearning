age = int(input('Age: '))
print(f'You are {age} years old')

try:
    age = int(input('Age: '))
    print(f'You are {age} years old')
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('Invalid input')