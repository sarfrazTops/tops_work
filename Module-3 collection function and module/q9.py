#(9)Write a Python function that takes two lists and returns true if they have
 #at least one common member.

#ans:-
def have_common_memmber(list1,list2):
    set1=set(list1)
    set2=set(list2)
    return not set1.isdisjoint(set2)
list1=[1,2,3,4]
list2=[5,6,7,3]
print(have_common_member(list1,list2))
