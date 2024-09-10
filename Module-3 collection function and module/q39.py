#Q.39 write a python script to merge two python dictionaries.

dict1={'a':1,'b':2}
dict2={'b':3,'c':4}
dict=dict1.copy()
dict.update(dict2)
print(dict)
