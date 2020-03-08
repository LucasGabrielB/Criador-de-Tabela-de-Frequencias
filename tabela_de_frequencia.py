#  -*- coding: utf-8 -*-
#
# Author: Lucas Gabriel B

import tkinter as tk
from tkinter import ttk

def make_calculations():
    ''' makes all calculations 
        (frequency table, standard deviation, coefficient of variation)
        and update data in the screen'''
    
    # clean the frequency table
    frequency_table.delete(*frequency_table.get_children())
    
    # read the data  of the file and save in a sorted list
    with open('dados.txt', 'r') as file:
        data = [float(i.replace(',', '.')) for i in file.readlines()]

    data.sort()

    # count the frequencies of each number
    # saves in dictionary
    frequencies = dict()
    for n in data:
        if n in frequencies:
            frequencies[n] += 1
        else:
            frequencies[n] = 1             
    
    # calculate the frequency table
    fr = fa = fra = 0
    for value, frequency in frequencies.items():
        total_of_data = len(data)
        
        # calculate the relative frequency
        fr = round((frequency / total_of_data) * 100, 2)

        # calculate cumulative frequency
        fa += frequency

        # calculate cumulative relative frequency
        fra += fr

        # add the line with the results
        frequency_table.insert("", "end", values=(value, frequency, f'{fr} %', fa, f'{round(fra, 2)} %'))
    
    # calculates the average of the data
    average = sum(data) / len(data)
    
    temp = list()
    # calculates the sum of (avarage - x)**2
    for value in data:
        temp.append((average - value) ** 2)

    # calculates the standard deviation
    standard_deviation = round((sum(temp) / (len(data) - 1)) ** 0.5, 2)

    # calculate the coefficient of variation of the read data
    coefficient_of_variation = round(standard_deviation / average * 100, 2)
   
    # create a formatd string for show in the screen
    standard_deviation_txt,  coefficient_of_variation_txt = f'Desvio Padrão: {standard_deviation}', f'Coeficiente de variação: {coefficient_of_variation} %'

    # creat/update the labels
    SDLabel = tk.Label(screen, text = standard_deviation_txt, font = ('Arial', 13)).grid(row = 3, columnspan = 3)
    CVLabel = tk.Label(screen, text = coefficient_of_variation_txt, font = ('Arial', 13)).grid(row = 4, columnspan = 3)


# create the screen
screen = tk.Tk()
screen.title('Criador De Tabela De Frequência Simples')

# create a title
titleLabel = tk.Label(screen, text='Tabela de frequências', font = ("Arial",30)).grid(row = 0, columnspan = 2)

# create Treeview with 5 columns
cols = ('X','Frequência Absoluta', 'Frequência Relativa %', 'Frequência Absoluta Acumulada', 'Frequência Relativa Acumulada %')
frequency_table = ttk.Treeview(screen, columns = cols, show = 'headings')

# set column headings
for col in cols:
    frequency_table.heading(col, text = col)

frequency_table.grid(row = 1, column = 0, columnspan = 2)

# call the function to calculate and show the frequency_table
make_calculations()

# add a roload button
reloadButton = tk.Button(screen, text='Recarregar', width = 15, command = make_calculations).grid(row = 5, column = 0)

#add a exit button
closeButton = tk.Button(screen, text = 'Sair', width = 15, command = exit).grid(row = 5, column = 1)

# create the main loop for the screen
screen.mainloop()
