import collections
s = 'python programming'

'''p = 2
y = 1
t = 1
h = 1
o = 2
n = 2
' ' = 1
r = 2
g = 2
a = 1
m = 2
i = 1'''

'''res = { }
for i in s:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1
print(res)'''

res = collections.defaultdict(int)
for i in s:
    res[i] += 1
print(res)