# Q13.Write a Python program to sum all the items in a dictionary.


n=int(input("enter the number:"))
d={}
for i in range(0,n,1):
    k=input("enter the key:")
    v=int(input("enter the value:"))
    d.update({k:v})
print("my dictionary",d)
svalues=sum(d.values())
print("sum of values",svalues)    