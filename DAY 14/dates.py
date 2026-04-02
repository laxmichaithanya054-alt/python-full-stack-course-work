from datetime import date,time,datetime

today = date.today()

print(today)
print(date(2026,3,31))

print("Year:",today.year)
print("Month:",today.month)
print("Day:",today.day)
print(today.weekday())
print(today.isoweekday())