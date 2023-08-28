weight = input('enter weight in pounds: ')
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
    weight = int(weight) * 0.45359237
    print('Your weight is ' + str(weight) + ' kilograms')
else:
    weight = int(weight)
    print('Your weight is ' + str(weight) + ' pounds')
