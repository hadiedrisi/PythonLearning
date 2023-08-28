customer = {
    'name': 'Hadi',
    'age': 30,
    'age': 30,
    'is_verified': True
}
customer['birthdate'] = 1994
print(
    customer.get('Name')
)

phone = input("Phone: ")
digit_dictionary = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '0': 'Zero'
}

for digit in phone:
    print(digit_dictionary[digit], end=' ')


emojies = {
    'smile': u'\U0001F600',
    'laugh': u'\U0001F602',
    'tongue': u'\U0001F61B',
    'cry': u'\U0001F62D',
}
