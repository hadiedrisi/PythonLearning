
def greet_user(name):
    print('Hello')
    print('Hi there')
    print(name)

print('Start')
greet_user("hadi")
print('Finish')





# keyword arguments
def user(first_name, last_name):
    print(f'hi {first_name} {last_name}')

user(last_name="hadi", first_name="edrisi")


def square(number):
    return number ** 2

print(square(2))

# return None