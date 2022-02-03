# Q17.Write a Python program to sort a dictionary by key.

from typing import OrderedDict

dict = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32'}
dict1=OrderedDict(sorted(dict.items()))
print(dict1)

