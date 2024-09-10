#(16)Write a Python program to check whether a list contains a sub list .


list = [1, 2, 3, 4, 5, 6]
sublist = [3, 4]
sublist_len = len(sublist)

if sublist_len == 0:
    print("The main list contains the sublist (sublist is empty).")
else:

    found = False
    
    
    for i in range(len(list) - sublist_len + 1):
        
        if list[i:i + sublist_len] == sublist:
            found = True
            break
    
    if found:
        print("The main list contains the sublist.")
    else:
        print("The main list does not contain the sublist.")
