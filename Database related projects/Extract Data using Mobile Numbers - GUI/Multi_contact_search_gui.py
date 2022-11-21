import tkinter as tk
from tkinter import *
import pandas as pd
from tkinter.filedialog import askopenfile,askopenfilename
import pymysql
from sqlalchemy import create_engine
import csv
import time


master = Tk()
master.title('Multi Contact Data Fetch Gui')

def Fetch_data():
    r_label = tk.Label(master, text='Connecting',bg='lightgreen', height=2, width=40)
    r_label.pack(pady=5)
    pymysql.install_as_MySQLdb()
    engine = create_engine('mysql+mysqldb://user:@localhost/vaibhav?charset=utf8')


    # database connection
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="test")
    cursor = connection.cursor()

    r_label["text"] = "Connected"

    file2=middle_entry.get()
    if input_entry.get()=='.txt':
        file1 = open(input_entry.get(), 'r')
        mobiles=file1.readlines()
        r_label["text"] = "Connected & Working on file"
        print('working on contact files')
        result = list()
        column_names = list()
        count = 1
        for mobile in mobiles:

            mobile = mobile.replace('\n', '').replace(' ', '')
            print(mobile)
            sql="SELECT * FROM `maintable` WHERE TELEPHONE_NUMBER={mobile} or ALTERNATE_PHONE_NO={mobile}".format(mobile=mobile)
            #sql = "SELECT * FROM `maintable` WHERE LOCAL_ADDRESS LIKE '%{pincode}%' or PERMANENT_ADDRESS LIKE '%{pincode}%' ".format(pincode=pincode)

            cursor.execute(sql)
            # fetch all the matching rows
            rows = cursor.fetchall()


            if count==1:
                for i in cursor.description:
                    column_names.append(i[0])

                result.append(column_names)

                for row in rows:
                    result.append(row)
                    print('1')

            else:
                for row in rows:
                    result.append(row)
                    print('else add')


            print (result)

            count += 1
            # Write result to file.
        now=time.strftime('%d-%m-%Y_%Hh-%Mm-%Ss')
        with open(output_entry.get()+'/contact_fetch_{now}.csv'.format(now=now), 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in result:
                csvwriter.writerow(row)
        cursor.close()
        r_label["text"] = "Task Completed"
        begin_button['bg']='light green'
        begin_button['text']='Completed'
        begin_button['state']='disable'

    elif middle_entry.get() != '':
        file2 = middle_entry.get()
        numbers=file2.split(',')
        print('working on contact files')
        result = list()
        column_names = list()
        count = 1
        for mobile in numbers:

            mobile = mobile.replace('\n', '').replace(' ', '')
            print(mobile)
            sql = "SELECT * FROM `maintable` WHERE TELEPHONE_NUMBER={mobile} or ALTERNATE_PHONE_NO={mobile}".format(
                mobile=mobile)
            # sql = "SELECT * FROM `maintable` WHERE LOCAL_ADDRESS LIKE '%{pincode}%' or PERMANENT_ADDRESS LIKE '%{pincode}%' ".format(pincode=pincode)

            cursor.execute(sql)
            # fetch all the matching rows
            rows = cursor.fetchall()

            if count == 1:
                for i in cursor.description:
                    column_names.append(i[0])

                result.append(column_names)

                for row in rows:
                    result.append(row)
                    print('1')

            else:
                for row in rows:
                    result.append(row)
                    print('else add')

            print(result)

            count += 1
            # Write result to file.
        now = time.strftime('%d-%m-%Y_%Hh-%Mm-%Ss')
        with open(output_entry.get() + '/contact_fetch_{now}.csv'.format(now=now), 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in result:
                csvwriter.writerow(row)
        cursor.close()
        r_label["text"] = "Task Completed"
        begin_button['bg'] = 'light green'
        begin_button['text'] = 'Completed'
        begin_button['state'] = 'disable'


def input():
    input_path = tk.filedialog.askopenfilename(filetypes=[("text file", "*.txt")])
    input_entry.delete(1, tk.END)  # Remove current text in entry
    input_entry.insert(0, input_path)  # Insert the 'path'


def output():
    path = tk.filedialog.askdirectory()
    output_entry.delete(1, tk.END)  # Remove current text in entry
    output_entry.insert(0, path)  # Insert the 'path'

def exit_commond():
    master.destroy()

top_frame = tk.Frame(master)
bottom_frame = tk.Frame(master)
middle_frame = tk.Frame(master)

line = tk.Frame(master, height=1, width=400, bg="grey80", relief='groove')

exit_button = tk.Button(top_frame, text="Exit", command=exit_commond)
exit_button.pack(pady=2)

input_path = tk.Label(top_frame, text="Input Contact File Path:")
input_entry = tk.Entry(top_frame, text="", width=40)
browse1 = tk.Button(top_frame, text="Browse", command=input)

output_path = tk.Label(bottom_frame, text="Output File Path:")
output_entry = tk.Entry(bottom_frame, text="", width=40)
browse2 = tk.Button(bottom_frame, text="Browse", command=output)

begin_button = tk.Button(bottom_frame, text='Begin!', command=lambda:Fetch_data())

top_frame.pack(side=tk.TOP)
line.pack(pady=10)

############################

middle_path = tk.Label(top_frame, text="Input Contact and separate by ' , ' symbol:")
middle_entry = tk.Entry(top_frame, text="", width=40)



top_frame.pack(side=tk.TOP)
line.pack(pady=10)
###############################

bottom_frame.pack(side=tk.BOTTOM)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)

middle_path.pack(pady=5)
middle_entry.pack(pady=5)


output_path.pack(pady=5)
output_entry.pack(pady=5)
browse2.pack(pady=5)

begin_button.pack(pady=20, fill=tk.X)


master.mainloop()