exp = input()
if '+' in exp:
    a,b = exp.split('+')
    print(add(int(a),int(b)))

exp = input()
if '-' in exp:
    a,b = exp.split('-')
    print(sub(int(a),int(b)))
    
exp = input()
if '*' in exp:
    a,b = exp.split('*')
    print(mul(int(a),int(b)))
    
exp = input()
if '/' in exp:
    a,b = exp.split('/')
    print(div(int(a),int(b)))
    
exp = input()
if '%' in exp:
    a,b = exp.split('%')
    print(mod(int(a),int(b)))
