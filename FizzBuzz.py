def checkio(number):
    if number % 5 ==0 and number % 3 == 0:
        return "Fizz Buzz"
    if number % 5 == 0:
        return "Buzz"
    if number % 3 == 0:
        return "Fizz"
    else:
        return str(number)
    return str(number)

print checkio(15)