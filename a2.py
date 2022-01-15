def Merge(dict1, dict2):
    return(dict1.update(dict2))
     
# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
 
# This return None
Merge(dict1, dict2)
 
# changes made in dict2
print(dict1)