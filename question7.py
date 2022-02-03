# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4=dic1.copy()
dic4.update(dic2)
dic4.update(dic3)
print(dic4)



# dict={1:'red',2:'green',3:'black',4:'white',5:'black'}
# new_list=[]
# for i in dict:
#     c=[i,dict[i]]
#     new_list.append(c)
# print(new_list) 

# list=[1,2,3,4,8,10,40]
# b={}
# for i in list:
#     b.update(i)
# print(b)    


# list1=[1,2,3,4]
# list2=['one','two','three','four']
# b={}
# i = 0
# for i in range(len(list1)):
#     b[list1[i]] = list2[i] 
# print(b)         


# list1=[1,2,3,4]
# list2=['one','two','three','four']
# list3={}
# for i in range(len(list1)):
#     list3.update({list1[i]:list2[i]})
# print(list3)    


# list1=[1,2,3,4,8,10,40]
# d1=dict(enumerate(list1))
# print(d1)

# list1=[1,2,3,4,5,6]
# d1=dict(enumerate(list1))
# print(d1)


list1=[1,2,3,4,5,6]
dic={}
i=0
for j in range(len(list1)):
    dic[i]=list1[j]
    i+=1
print(dic)
    