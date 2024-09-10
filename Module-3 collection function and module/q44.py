#(44)Write a Python program to create and display all combinations of letters,
      #selecting each letter from a different key in a dictionary.
     
dict = {
    '1': ['a', 'b'],
    '2': ['c', 'd'],
}
l=list(dict.values())
for com in l[1:]:
    for i in l[0]:
        for s in com:
            print(i+s)
