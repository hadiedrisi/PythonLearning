i = 1
while i < 10:
    print('*'*i)
    i += 1

print("Done")


secret_number = 9
guess_count = 3
while guess_count > 0:
    guess = int(input("Guess: "))
    if guess == secret_number:
        print("You Won")
        break

    else:
        guess_count -= 1
        print("Wrong")



print(""" 
Welcome to the rollercoaster
start - to start
stop - to stop                    
""")        
