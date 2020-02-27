#  -*- coding: utf-8 -*-
#
# Author: Lucas Gabriel B


# colect the data and save in a sorted list 
data = [int(i) for i in input().strip().split()]
data.sort()

# count the frequencies of each number
# saves in dictionary
frequencies = dict()
for n in data:
    if n in frequencies:
        frequencies[n] += 1
    else:
        frequencies[n] = 1

# write a table with the results in the console

# print the header
print(f'X\t|f\t|fa\t|fr\t|fra')
print('-' * 40)

fr = fa = fra = 0
for value, frequency in frequencies.items():
    total_of_data = len(data)
    
    # calculate the relative frequency
    fr = int(round((frequency / total_of_data), 2) * 100)

    # calculate cumulative frequency
    fa += frequency

    # calculate cumulative relative frequency
    fra += fr

    # print the line with the results
    print(f'{value}\t|{frequency}\t|{fa}\t|{fr}%\t|{fra}%')

print('-' * 40)
