from tkinter import *
from PIL import ImageTk,Image
import sqlite3
import pandas as pd
data=pd.read_excel('data.xlsx')

root= Tk()
root.title('Vaibhav Database')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x400")
#Databases
# Create a database or connect to one
cnx = sqlite3.connect('student_database')
data.to_sql(name='ipat_data', con=cnx, index=False)

p2 = pd.read_sql('select * from ipat_data', cnx)
print(p2)

print('done')
root.mainloop()