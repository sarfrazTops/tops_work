#Q.32 write a python script to sort (ascending and descending) a dictionary by value.

import operator
d={1: 2,3: 4,4:3,2:1,0:0}
print('original dictioary:',d)
sorted_d=sorted(d.items(),key=operator.itemgetter(0))
print('Dictionary in ascending order by value:',sorted_d)
sorted_d=sorted(d.items(),key=operator.itemgetter(0),reverse=True)
print('Dictionary in descending order by value:',sorted_d)
