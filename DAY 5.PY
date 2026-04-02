data ={
    "samba": {"status":True, "Python":99 , "Mysql":90, "Django":97},
    "satya": {"status":True, "Python":89 , "Mysql":81, "Django":85},
    "mani": {"status":True, "Python":79 , "Mysql":73, "Django":72},
    "uma": {"status":True, "Python":69 , "Mysql":76, "Django":65},
    "venky": {"status":True, "Python":59 , "Mysql":77, "Django":57},
    "pavan": {"status":True, "Python":49 , "Mysql":50, "Django":40},
    "jag": {"status":True, "Python":19 , "Mysql":20, "Django":25},
    "Chalapathi": {"status":False, "Python":None , "Mysql":None, "Django":None},
}

name=input("Enter the name of the student: ")
if name in data:
    if data[name]["status"]:
        sum = data[name]["Python"]+data[name]["Mysql"]+data[name]["Django"]
        avg=sum/3
        if avg>=90:
            print(f"Congrats {name}, you have secured the first rank")
        elif avg>=75:
             print(f"{name}, Good Keep it up for next time!")
        elif avg>=50:
            print(f"{name}, Work hard to gain the mark")
        else:
            print(f"{name }, you have failed in the exam bring your parents")
    else:
        print(f"{name} You have not written the exam please bring your parents")
else:
    print(f"{name} is not available in the records")
