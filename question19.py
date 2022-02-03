# Q19.
# Write a Python program to remove duplicates from Dictionary.
# student_data = {'id1':
# {'name': ['Sara'],
# 'class': ['V'],
# 'subject_integration': ['english, math, science']
# },
# 'id2':
# {'name': ['David'],
# 'class': ['V'],
# 'subject_integration': ['english, math, science']
# },
# 'id3':
# {'name': ['Sara'],
# 'class': ['V'],
# 'subject_integration': ['english, math, science']
# },
# 'id4':
# {'name': ['Surya'],
# 'class': ['V'],
# 'subject_integration': ['english, math, science']
# },
# }
# Sample output:
# {'id2': {'subject_integration': ['english, math, science'], 'class': ['V'], 'name': ['David']}, 'id4':
# {'subject_integration': ['english, math, science'], 'class': ['V'], 'name': ['Surya']}, 'id1':
# {'subject_integration': ['english, math, science'], 'class': ['V'], 'name': ['Sara']}}



student_data={'id1':
{'name':['sara'],
'class':['v'],
'subject_intergration':['english,math,science']
},
'id2':
{'name':['David'],
'class':['v'],
'subject_intergration':['english,math,science']
},
'id3':
{'name':['surya'],
'class':['v'],
'subject_intergrastion':['english,math,science']
},
'id4':
{'name':['surya'],
'class':['v'],
'subject_intergration':['english,math,science']
}
}
b={}
for key,value in student_data.items():
    if value not in b.values():
        b[key]=value
print(b)        