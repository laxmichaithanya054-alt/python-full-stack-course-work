import collections

s = 'python programming'
l = [1,2,3,4,5,6,2,3,4,5,23,6,8,8]
r = 'this is that that is this'.split()  #If split is not mentioned, then it takes each and every letter and counts

res  = collections.Counter(s)
res1 = collections.Counter(l)
res2 = collections.Counter(r)

print(res)
print(res1)
print(res2)
