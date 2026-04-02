i = 20
while i <=30:
    if i==25:
       continue
    print(i)
    i+=1


bullets = 10
while  bullets > 0:
    print(f'{bullets} bullets are left ,you can shoot!')
    bullets-=1
else:
    print("game over")


data = {}
n = int(input("enter the no of students"))
for i in range(n):
    name = input("enter the name: ")
    data[name]=False

    for name in data:
     print(name)
     status = int(input("enter the {name} status(0-Absent ,1-present): "))
     data[name]= bool(status)
print(data)
    


