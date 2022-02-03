# Q50.Write a Python program to convert a given dictionary into a list of lists.
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Convert the said dictionary into a list of lists:
# [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]


# dict={1:'red',2:'green',3:'black',4:'white',5:'black'}
# b=[]
# for key ,val  in dict.items():
#         b.append([key,val])
# print(b)    

dict={1:'red',2:'green',3:'black',4:'white',5:'black'}
new_list=[]
for i in dict:
    c=[i,dict[i]]
    new_list.append(c)
print(new_list)    

# dict1={'1':'Austin Little','2':'Natasha Howard','3':'Alfred Mullins','4':'jamie Rowe'}
# c=[]
# for key ,val in dict1.items():
#     c.append([key,val])
# print(c)    


dict1={'1':'Austin Little','2':'Natasha Howard','3':'Alfred Mullins','4':'jamie Rowe'}
new_list=[]
for i in dict1:
    k=[i,dict1[i]]
    new_list.append(k)
print(new_list)    