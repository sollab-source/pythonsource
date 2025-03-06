a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is c)     # True (a와 c는 같은 객체)
print(a is b)     # False (a와 b는 다른 객체, 값은 같지만)
print(a is not b) # True (a와 b는 다른 객체)