def gcd(m,n):
    if n==0:
        return m
    else:
        return gcd(n, m%n)
    
m,n = [float(x) for x in input("Enter the two numbers : ").split()]
print("GCD of {0}, {1} is {2}".format(m,n, gcd(m,n)))