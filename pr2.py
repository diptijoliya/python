name = input("enter name:")
age = int(input("enter age:"))
yage = 18 - (age)

if (age>18):
    print(name,"you can drive")
elif(age==18):
    print(name,"you can drive ")
else:
    print("you can  drive after",yage,"years")