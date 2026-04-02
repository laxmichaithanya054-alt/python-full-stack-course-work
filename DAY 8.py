products = ['rice','sugar','wheat flour','milk','eggs','cooking oil','tea powder','salt','bre...']
prices = [60,30,40,20,70,80,110,35,45,65]

print("------------welcome to grocery store--------")
print("here are the available products:\n")

print("index".ljust(5," "),"products".ljust(15," "),"price".ljust(5," "))

for i in range(len(products)):
    print(str(i+1).ljust(5," "),products[i].ljust(15," "),str(prices[i]).ljust(5," "))

items = list(map(int,input("enter the indexes:").split()))

print("selected items:")
total = 0
for item in items:
    print(products[item-1],prices[item-1])
    total+=prices[item-1]

print("\n total amount:",total)
      
    
