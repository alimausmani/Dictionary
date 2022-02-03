# Q22. Write a Python program to create and display all combinations of letters, selecting each
# letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd



from itertools import product
data={'1':['a','b'],'2':['c','d']}
for x,y in product(*data.values()):
    print(x+y)