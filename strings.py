course = 'Python for Beginners'
print(course)
print(course[-2])
print(course[0:3])
print(course[1:])
print(course[:5])
print(course[::2])
print(course[::-1])
print(course[::-2])
print(course[1:-1])

first = 'hadi'
last = 'edrisi'

message = f'Hello {first} [{last}], would you like to learn some Python today?'

print(message)

print(len(course))
result = course.upper()
print(result)
print(course.lower())

print(course.find('for'))
print(course.replace('for', 'four'))
print(course.find('o'))
print(course.count('o'))
print('Python' in course)
print(course.title())