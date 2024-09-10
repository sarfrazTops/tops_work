#(46)Write a Python program to combine values in python list of dictionaries.

from collections import Counter


data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
counter = Counter()


for entry in data:
    item = entry['item']
    amount = entry['amount']
    counter[item] += amount

print("Counter ({})".format(dict(counter)))
