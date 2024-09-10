#Q.33  write a python script to concatenate following dictionaries to create a new one.

dict1={'a':1,'b':2}
dict2={'b':1,'c':4}
dict3={'d':5}
dict4={}
for d in (dict1,dict2,dict3):dict4.update(d)
print(dict4)
