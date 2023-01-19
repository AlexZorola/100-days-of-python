#Print each number from 1 to 100 in order

#When the number is divisible by 3, then instead of printing the number it will print "Fizz".
#When the number is divisible by 5, then instead of printing the bumber it will print "Buzz".
#When the number is divisible by both 3 and 5, then instead of printing the number it will print "FizzBuzz".

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
