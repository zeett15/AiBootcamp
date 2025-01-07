# menetukan bilangan ganjil dan genap
def check (n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
    
def print_check(n):
    print (f"{n} is a {check(n)} number")
    
print_check(9)