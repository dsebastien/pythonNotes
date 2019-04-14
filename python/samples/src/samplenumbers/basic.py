import math
import random

def foo():
    print("cool")


print(123 + 222)
print(1.5 * 4)

# large_result = 2 ** 1000000
# print("Digits in the large result: " + str(len(str(large_result))))
# print(large_result)

print(3.1415 * 2)

print(math.pi)
print("Square root of 9: "+str(math.sqrt(9)))
print("Square 3: "+str(3 ** 2))
print("Square 4: "+str(4 ** 2))
print("Cube 2: "+str(2 ** 3))
print("Cube 3: "+str(3 ** 3))


def cubic_root(a):
    if 0 <= a:
        return a**(1./3.)
    return -(-a)**(1./3.)

print("Cubic root of 27: "+(str(cubic_root(27))))

print("Random: "+str(random.random()))

print("Random between 1 and 4: "+str(random.choice([1, 2, 3, 4])))
