import tkinter as tk
from tkinter import *
import pandas as pd
from tkinter.filedialog import askopenfile,askopenfilename
import pymysql
from sqlalchemy import create_engine
import csv


master = Tk()
master.title('Multi Pincode Data Fetch Gui')

def Fetch_data():
    r_label = tk.Label(master, text='Connecting',bg='lightgreen', height=2, width=40)
    r_label.pack(pady=5)
    pymysql.install_as_MySQLdb()
    engine = create_engine('mysql+mysqldb://user:@localhost/vaibhav?charset=utf8')


    # database connection
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="test")
    cursor = connection.cursor()

    r_label["text"] = "Connected"
    file1 = open(input_entry.get(), 'r')
    pincodes=file1.readlines()
    r_label["text"] = "Connected & Working on file"
    print('working on pincode files')
    for pincode in pincodes:
        pincode = pincode.replace('\n', '')
        print(pincode)
        # sql="SELECT * FROM `maintable` WHERE TELEPHONE_NUMBER={mobile} or ALTERNATE_PHONE_NO={mobile}".format(mobile=mobile)
        sql = "SELECT * FROM `maintable` WHERE LOCAL_ADDRESS LIKE '%{pincode}%' or PERMANENT_ADDRESS LIKE '%{pincode}%' ".format(pincode=pincode)

        cursor.execute(sql)
        # fetch all the matching rows
        rows = cursor.fetchall()

        result = list()
        column_names = list()

        for i in cursor.description:
            column_names.append(i[0])

        result.append(column_names)
        for row in rows:
            result.append(row)

        # Write result to file.
        with open(output_entry.get()+'/{pincode}.csv'.format(pincode=pincode), 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in result:
                csvwriter.writerow(row)
    cursor.close()
    r_label["text"] = "Task Completed"

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
line = tk.Frame(master, height=1, width=400, bg="grey80", relief='groove')

exit_button = tk.Button(top_frame, text="Exit", command=exit_commond)
exit_button.place(x=1, y=10, height=20,width=30)

input_path = tk.Label(top_frame, text="Input File Path:")
input_entry = tk.Entry(top_frame, text="", width=40)
browse1 = tk.Button(top_frame, text="Browse", command=input)

output_path = tk.Label(bottom_frame, text="Output File Path:")
output_entry = tk.Entry(bottom_frame, text="", width=40)
browse2 = tk.Button(bottom_frame, text="Browse", command=output)

begin_button = tk.Button(bottom_frame, text='Begin!', command=lambda:Fetch_data())

top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)

output_path.pack(pady=5)
output_entry.pack(pady=5)
browse2.pack(pady=5)

begin_button.pack(pady=20, fill=tk.X)


master.mainloop()