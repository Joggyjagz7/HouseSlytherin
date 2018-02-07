#  Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
#  Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
#  Enter 7, 2, bob, 10, and 4 and match the output below.

smallNo = 0
maxNo = 0

while True:
    res = input('Enter a Number: ')
    if res == 'done':
        break
    try:
        num = int(res)
        if maxNo < num:
            maxNo = num
        if smallNo == 0 or smallNo > num:
            smallNo = num

    except:
        print('Invalid input')

print('Maximum is', maxNo)
print('Minimum is', smallNo)
