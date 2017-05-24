
ELEMENTS = (("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
            ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
            ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1))


def checkio(number):
    result = ""
    for roman, n in ELEMENTS:
        if n <= number:
            result = result + roman * (number // n)
            number = number % n
    return result

print checkio(1666)  

print 1666 //1000
print ""+"M"*(1666//1000)