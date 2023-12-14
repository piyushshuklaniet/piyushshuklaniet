def reminder(divident,divisor):
    return divident%divisor
def division(divident,divisor):
    quotient = divident//divisor
    reminder = divident%divisor
    return (quotient,reminder)
def cube(n):
    return n**3
def isprime(number):
    for i in range(2,int(range**0.5)+1):
        if(range%i==0):
            return False
    return True


def ispythagorus(base,perp,hyp):
    if(hyp**2 == ((base**2)+(perp**2))):
        return True
    return False

