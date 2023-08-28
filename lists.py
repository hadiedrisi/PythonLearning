names = ['john', 'hadi', 'ahmad', 'ali', 'mohammad']
print(names)
print(names[0])
print(names[2:4])
print(names[1:])
print(names[:])

numbers = [1, 2, 5, 3, 10, 4]
max = numbers[0]
for number in numbers:
    if (number > max):
        max = number

print(max)


# 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0])
print(matrix[0][1])

# list methods
numbers.remove(1)
print(numbers)

numbers.append(20)
print(numbers)

numbers.sort()
print(numbers)

numbers.insert(0, 10)
print(numbers)

numbers.pop()
print(numbers)

print(50 in numbers)

print(numbers.count(5))

numbers2 = numbers.copy()

numbers2.append(20)
numbers2.append(30)
print(numbers2)

unique = []
for item in numbers2:
    duplicated = 0
    for item2 in numbers2:
        if (item == item2):
            duplicated += 1
    if (duplicated == 1):
        unique.append(item)

print(unique)


for item in numbers2:
    if (item not in unique):
        unique.append(item)

print(unique)