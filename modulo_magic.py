"""Calculating (n! mod m) by using following modulo properties"""

# ( a + b ) mod m = ( a mod m + b mod m ) mod m
# ( a − b ) mod m = ( a mod m − b mod m ) mod m
# ( a · b ) mod m = ( a mod m · b mod m ) mod m

x = 1
n = 5
m = 9
for i in range(2, n + 1):
    # no need to calculate factorial (large number)
    x = (x * i) % m
print(x)
