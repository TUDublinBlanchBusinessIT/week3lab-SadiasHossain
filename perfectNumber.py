#Sadia Hossain
#07 February 2024
#perfectNumber.py

from divisors import divisors

def perfectNumber (x):
    result = False
    sumDivisors = sum(divisors(x))
    if sumDivisors == x :
        result = True
    return result
