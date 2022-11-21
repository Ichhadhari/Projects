from tkinter import *
from PIL import ImageTk,Image
import sqlite3
import pandas as pd
data=pd.read_excel('data.xlsx')
data['mobile_available'] = ''
for m in range(len(data['MOBILE_NO'])):
    mobile=str(data.iloc[m,20])
    mobile=mobile.replace('NaN', '').replace(' ', '').replace('_', '').replace('nan', '').replace('+', '')

    data.iloc[m, 20]=mobile
    if len(mobile) == 10 or len(mobile) == 12 or len(mobile) == 13 or (mobile[-2:]=='.0'):
        data.iloc[m, 20]=mobile[-12:-2]
        print(len(data.iloc[m, 20]))
        if data.iloc[m, 20] != '':
            data.iloc[m, -1] = 'Available'
            print(data.iloc[m, -1])
    else:
        data.iloc[m, -1] = 'Not_Available'
        print(data.iloc[m, -1])

print(data['MOBILE_NO'])

print(data['mobile_available'].value_counts().to_frame())
print(data['AGE'].value_counts())
data['Age_Between'] = ''
for i in range(len(data)):
    number = int(data.iloc[i, 10])
    if number <= 20:
        data.iloc[i, -1] = 'first time V'

    elif number <= 21 or number >= 25:
        data.iloc[i, -1] = '21 to 25'

    elif number <= 26 or number >= 30:
        data.iloc[i, -1] = '25 to 30'

    elif number <= 31 or number >= 35:
        data.iloc[i, -1] = '31 to 35'

    elif number <= 36 or number >= 40:
        data.iloc[i, -1] = '36 to 40'

    elif number <= 41 or number >= 45:
        data.iloc[i, -1] = '41 to 45'

    elif number <= 46 or number >= 50:
        data.iloc[i, -1] = '46 to 50'

    elif number <= 51 or number >= 55:
        data.iloc[i, -1] = '51 to 55'

    elif number <= 55 or number >= 60:
        data.iloc[i, -1] = '55 to 60'
    elif number <= 60 :
        data.iloc[i, -1] = 'senior citien'

data['Activity']=''

root= Tk()
root.title('Vaibhav Database')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x400")
#Databases
# Create a database or connect to one
cnx = sqlite3.connect('test_database')
data.to_sql(name='data1', con=cnx, index=False)

p2 = pd.read_sql('select * from data1', cnx)
print(p2)

print('done')
root.mainloop()