from ast import Break
import random

number = random.randint(1,9)
guess = input("your Number: ")
chances = 5



if guess!=number:
    chances=chances-1
    print("the number is greater than: ", number-3)
    guess = input("your Number: ")
    chances=chances-1
    if guess == number:
        print('Congratulations YOU WON!!!')

    print("the number is less than: ", number+1)
    guess = input("your Number: ")
    chances=chances-1
    if guess == number:
        print('Congratulations YOU WON!!!')
        
    print("the number is greater than: ", number-5)
    guess = input("your Number: ")
    chances=chances-1
    if guess == number:
        print('Congratulations YOU WON!!!')
        
    print("the number is less than: ", number+4)
    guess = input("your Number: ")
    chances=chances-1
    if guess == number:
        print('Congratulations YOU WON!!!')
        
    print("the number is greater than: ", number-2)
    guess = input("your Number: ")
    if guess == number:
        print('Congratulations YOU WON!!!')
    
    

if chances == 0:
    print("YOU LOSE!!! The number is: ", number)
    

