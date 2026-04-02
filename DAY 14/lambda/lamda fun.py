def add (a,b,c):
    return (a+b+c)/3

add1=lambda a,b,c:(a+b+c)/3

print(add(1,2,3))
print(add1(6,7,8))

iseven1 = lambda n:  "even" if n%2==0 else "odd"

print(iseven1(19))
print(iseven1(18))

isgreater = lambda a,b:  "a is greater" if a>b else "b is greater"
print(isgreater(10,20))
print(isgreater(30,20))
print("------------------------------------")

l=["samba","satya","mani","uma"]
res = list(map(lambda i:i.title(),l))
print(res)

l = [20,30,40,50]
res = list(map(lambda i:i%3==0,l))
print(res)

from functools import reduce
l = [1,2,3,4,5]
res = reduce(lambda a,b:a*b,l)
print(res)


