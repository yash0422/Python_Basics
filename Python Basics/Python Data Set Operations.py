# To handle data sets (csv file), firstly you need to import pandas module

import pandas as pd
import csv

dataset = pd.read_csv("List of cities with longitude and latitude.csv")

for row in dataset:
    print(row)
#csv_reader



#print(dataset.dtypes)          # shows colmun data types is str, int, float etc.
#print(dataset.keys())           # shows column names
#print(dataset.head())           # shows first 5 rows
#print(dataset.count(0))         # shows number of entries in column
#print(dataset.count(1))         # shows number of entries in rows
#print(dataset.describe())       # describes the data



'''
import tkinter as tk
from tkinter import filedialog
import pandas as pd

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
canvas1.pack()

def getCSV():
    global df

    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv(import_file_path)
    print(df)

browseButton_CSV = tk.Button(text="      Import CSV File     ", command=getCSV, bg='green', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_CSV)

root.mainloop()
'''

