from pandastable import Table, TableModel

import numpy as np
import pandas as pd
from fpdf import FPDF
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter.ttk import Combobox
import time
import sqlite3
from PIL import ImageTk, Image

class Dashboard:
    def __init__(self, window,data_all):

        self.data_all=data_all

        self.window = window
        self.window.title('Student Info')
        self.window.geometry('1200x750')
        self.window.state('zoomed')
        self.window.resizable(0, 0)
        self.window.config(background='#eff5f6')
        self.sidebar = Frame(self.window, bg='#ffffff')
        self.sidebar.place(x=0, y=0, width=250, height=750)

        # Name of brand/person
        self.brandName = Label(self.sidebar, text='iPAT Students', bg='#ffffff', font=("", 15, "bold"))
        self.brandName.place(x=50, y=100)

        # option

        # Dashboard
        self.dashboard_text = Button(self.sidebar, text='>Student Entry', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                     cursor='hand2', activebackground='#ffffff',
                                     command=lambda: self.show_frame(self.frame1))
        self.dashboard_text.place(x=50, y=190)

        # Filter

        self.manage_text = Button(self.sidebar, text='>Student Info', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff',
                                  command=lambda: self.show_frame(self.frame2))
        self.manage_text.place(x=50, y=220)


        # EXIT
        self.exit_text = Button(self.sidebar, text='>Exit', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff', command=self.Exit)
        self.exit_text.place(x=50, y=250)
        # ======= TIME AND DATE ============

        self.date_time = Label(self.window)
        self.date_time.place(x=50, y=15)
        self.show_time()

        # basic frame
        self.frame1 = Frame(self.window, bg='light blue')
        # self.frame1.place(x=220, y=1, width=750, height=800)

        self.frame2 = Frame(self.window, bg='white')
        # self.frame2.place(x=220, y=1, width=750, height=800)

        self.frame3 = Frame(self.window, bg='white')
        # self.frame3.place(x=220, y=1, width=750, height=800)

        for frame in (self.frame1, self.frame2, self.frame3):
            frame.place(x=200, y=1, width=1100, height=900)



        # frame 1

        self.q1 = Label(self.frame1, text='Student Name:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
        self.q1.place(x=100, y=210, height=30,width=200)

        self.a1=Entry(self.frame1, bd=1, font=("", 10, "bold"))
        self.a1.place(x=350, y=210, height=30, width=350)

        self.q2 = Label(self.frame1, text='Mail ID:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
        self.q2.place(x=100, y=245, height=30, width=200)

        self.a2 = Entry(self.frame1, bd=1,font=("", 10, "bold"))
        self.a2.place(x=350, y=245, height=30, width=350)

        self.q3 = Label(self.frame1, text='Mobile no.:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
        self.q3.place(x=100, y=280, height=30, width=200)

        self.a3 = Entry(self.frame1, bd=1,font=("", 10, "bold"))
        self.a3.place(x=350, y=280, height=30, width=350)

        self.q4 = Label(self.frame1, text='Aadhar No.:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
        self.q4.place(x=100, y=315, height=30, width=200)

        self.a4 = Entry(self.frame1, bd=1,font=("", 10, "bold"))
        self.a4.place(x=350, y=315, height=30, width=350)

        self.q5 = Label(self.frame1, text='Address:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
        self.q5.place(x=100, y=350, height=30, width=200)

        self.a5 = Entry(self.frame1, bd=1, font=("", 10, "bold"))
        self.a5.place(x=350, y=350, height=30, width=350)

        self.q6 = Label(self.frame1, text='Batch:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
        self.q6.place(x=100, y=385, height=30, width=200)

        self.a6 = Entry(self.frame1, bd=1, font=("", 10, "bold"))
        self.a6.place(x=350, y=385, height=30, width=350)

        self.q7 = Label(self.frame1, text='Course', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
        self.q7.place(x=100, y=420, height=30, width=200)

        self.a7 = Entry(self.frame1, bd=1, font=("", 10, "bold"))
        self.a7.place(x=350, y=420, height=30, width=350)

        self.q8 = Label(self.frame1, text='Mr/Mrs Name Surname', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
        self.q8.place(x=100, y=455, height=30, width=200)

        self.a8 = Entry(self.frame1, bd=1, font=("", 10, "bold"))
        self.a8.place(x=350, y=455, height=30, width=350)

        self.q9 = Label(self.frame1, text='Assistant-Officer', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
        self.q9.place(x=100, y=490, height=30, width=200)

        self.a9 = Entry(self.frame1, bd=1, font=("", 10, "bold"))
        self.a9.place(x=350, y=490, height=30, width=350)


        #button sumbmit

        self.add = Button(self.frame1, text='Add-Data & Generate PDF',font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff', command=self.Adddata_createpdf)
        self.add.place(x=350, y=530, height=30, width=300)

        self.add_only_data = Button(self.frame1, text='Add-Data', font=("", 13, "bold"), bd=0,
                          cursor='hand2', activebackground='#ffffff', command=self.add_only)
        self.add_only_data.place(x=200, y=530, height=30, width=100)

        self.add_only_pdf = Button(self.frame1, text='Create PDF', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff', command=self.create_pdf)
        self.add_only_pdf.place(x=700, y=530, height=30, width=100)



        #################################### FRAME 2 ##########################
        self.show = Button(self.frame2, text='Show All Student detail', font=("", 13, "bold"), bd=0,bg='light blue',
                          cursor='hand2', activebackground='#ffffff', command=self.show_details)
        self.show.place(x=250, y=30, height=30, width=300)



        #loop
        window.mainloop()

    ################################################################## methods

    def Adddata_createpdf(self):
        self.add_only()
        self.create_pdf()
        self.add['bg'] = 'light green'
        self.add['text'] = 'see result'


    def show_details(self):
        cnx = sqlite3.connect('student_database')
        self.data_all = pd.read_sql('select * from ipat_data', cnx)
        print(self.data_all.columns)
        cnx.commit()
        cnx.close()

        self.Filter_subframe = Frame(self.frame2, bg='white')
        self.Filter_subframe.place(x=2, y=70, width=1000, height=700)

        self.table = pt = Table(self.Filter_subframe, dataframe=self.data_all, showtoolbar=True,
                                showstatusbar=True)
        pt.show()

        self.Export = Button(self.frame2, text='Export', font=("", 13, "bold"), bd=0, bg='light blue',
                             cursor='hand2', activebackground='#00ffff', command=self.export)
        self.Export.place(x=670, y=30)


    def export(self):
        print('output in Downloads folder')
        d = str(self.date)
        d = d.replace('/', '')
        d = d + str(self.time)
        d = d.replace(':', '')
        print(self.data_all.head())
        self.data_all.to_csv(r"C:/Users/admin/Downloads/output_{d}.csv".format(d=d), index=False)
        self.Export['bg'] = 'light green'

    def add_only(self):
        data1 = self.a1.get()
        data2 = self.a2.get()
        data3 = self.a3.get()
        data4 = self.a4.get()
        data5 = self.a5.get()
        data6 = self.a6.get()
        data7 = self.a7.get()
        data8 = self.a8.get()
        data9 = self.a9.get()
        demo_date = str(self.date)
        date = demo_date[-2:] + '/' + demo_date[-5:-3] + '/' + demo_date[:4]

        if (data1 != '') & (data2 != '') & (data3 != '') & (data4 != '') & (len(data3) == 10) & (len(data4) == 12) & (data5 != ''):
            conn = sqlite3.connect('student_database')
            # Create cursor.
            c = conn.cursor()
            # Create table
            c.execute(
                """INSERT INTO ipat_data VALUES (:v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9)""",
                {
                    'v1': data1,
                    'v2': data2,
                    'v3': data3,
                    'v4': data4,
                    'v5': data5,
                    'v6': data6,
                    'v7': data7,
                    'v8': data8,
                    'v9': data9,

                }
                )
            # Commit Changes
            conn.commit()
            # Close Connection
            conn.close()

            self.add_only_pdf['bg'] = 'light green'
            self.add_only_pdf['text'] = 'Done !'

        else:
            self.add_only_pdf['bg']='red'
            self.add_only_pdf['text'] = 'try again'


    def create_pdf(self):


        data1=self.a1.get()
        data2 = self.a2.get()
        data3 = self.a3.get()
        data4 = self.a4.get()
        data5 = self.a5.get()
        data6 = self.a6.get()
        data7=self.a7.get()
        data8 = self.a8.get()
        data9 = self.a9.get()
        demo_date=str(self.date)
        date=demo_date[-2:]+'/'+demo_date[-5:-3]+'/'+demo_date[:4]

        if (data1 != '') & (data2 != '') & (data3 != '') & (data4 != '')&(len(data3)==10) &(len(data4)==12)& (data5 != ''):

            pdf = FPDF(orientation='P', unit='mm', format='A4')

            # Add a Unicode free font
            pdf.add_font('OpenSans', '', r'H:\vaibhav\PycharmProjects\Automation_pdf _database\Font\open\OpenSans-Bold.ttf', uni=True)
            # page1



            pdf.add_page()
            pdf.set_font('OpenSans', 'U', 12)
            pdf.set_text_color(187,66,40)
            pdf.image(r'background/nda1.jpg', x=0, y=0, w=210, h=297)
            # txt = 'Mr. vaibhav rokde'
            pdf.set_xy(129.2, 67)
            pdf.cell(0, 12, date, ln=1, align='L')

            pdf.add_font('OpenSans', '',r'H:\vaibhav\PycharmProjects\Automation_pdf _database\Font\open\OpenSans-BoldItalic.ttf', uni=True)
            pdf.set_xy(24.8, 171.5)
            pdf.cell(0, 12, data1, ln=1, align='L')

            # page 2
            pdf.add_page()
            pdf.add_font('OpenSans', '',r'H:\vaibhav\PycharmProjects\Automation_pdf _database\Font\open\OpenSans-Bold.ttf',uni=True)
            pdf.set_font('OpenSans', '', 12)
            pdf.set_text_color(187,66,40)
            pdf.image(r'background/nda2.jpg', x=0, y=0, w=210, h=297)
            # txt = 'Mr. vaibhav rokde'
            pdf.set_xy(33, 212.8)  #name
            pdf.cell(0, 10, data1, ln=1, align='L')
            pdf.set_font('OpenSans', '', 10)
            pdf.set_xy(32.5, 232.5) #date
            pdf.cell(0, 9, date, ln=1, align='L')

            pdf.set_xy(35.5, 242) #address
            pdf.cell(0, 9, data5, ln=1, align='L')

            pdf.set_xy(62.5, 246.7)  # adhar
            pdf.cell(0, 9, data4, ln=1, align='L')


            #page 3

            pdf.add_page()
            pdf.add_font('Lato', '',
                         r'H:\vaibhav\PycharmProjects\Automation_pdf _database\Font\Lato2OFL\Lato-Bold.ttf', uni=True)
            pdf.set_font('Lato', '', 16)
            pdf.set_text_color(252, 252, 252)
            # back ground
            pdf.image(r'background/file_cover.jpg', x=0, y=0, w=210, h=297)
            # pdf.image(r'background/images.jpg', x = 0, y = 0, w = 2480, h = 3508)
            txt = data1  # 'Mr. vaibhav rokde'
            pdf.set_xy(0, 42.2)
            pdf.cell(195.4, 14, data2, ln=1, align='R')

            pdf.add_font('Lato', '',
                         r'H:\vaibhav\PycharmProjects\Automation_pdf _database\Font\Lato2OFL\Lato-Bold.ttf', uni=True)
            pdf.set_font('Lato', '', 16)
            pdf.set_text_color(252, 252, 252)
            txt = data2  # 'Mr. vaibhav rokde @ gamil'
            pdf.set_xy(0, 50)
            #pdf.image(r'background/side_cover.jpg', x=135, y=60, w=30, h=35)
            pdf.cell(195.4, 12, data3, ln=1, align='R')

            pdf.add_font('Lato', '',
                         r'H:\vaibhav\PycharmProjects\Automation_pdf _database\Font\Lato2OFL\Lato-Thin.ttf', uni=True)
            pdf.set_font('Lato', '', 13)#batchLato-Regular
            pdf.set_text_color(252, 252, 252)
            batch_str='Batch '+ time.strftime('%B, %Y')
            pdf.set_xy(0, 18)

            if data6=='':
                pdf.cell(195.4, 12, batch_str, ln=1, align='R')
            else:
                pdf.cell(195.4, 12, data6, ln=1, align='R')

            pdf.add_font('league', '',
                         r'H:\vaibhav\PycharmProjects\Automation_pdf _database\Font\name\league-spartan.bold.ttf', uni=True)


            name_spt=data1.split(' ')
            fix=45
            if len(name_spt[0])<=8:
                pdf.set_font('league', '', fix)
                pdf.set_text_color(252, 252, 252)
                pdf.set_xy(18, 105)
                pdf.cell(195, 45, name_spt[0].upper(), ln=1, align='L')
            else:
                pdf.set_font('league', '', fix-len(name_spt[0])//2)
                pdf.set_text_color(252, 252, 252)
                pdf.set_xy(18, 105)
                pdf.cell(195, 45, name_spt[0].upper(), ln=1, align='L')

            if len(name_spt)>=2:

                if len(name_spt[-1]) <= 8:
                    pdf.set_font('league', '', fix)
                    pdf.set_text_color(252, 252, 252)
                    pdf.set_xy(18, 128)
                    pdf.cell(195, 45, name_spt[-1].upper(), ln=1, align='L')
                else:
                    pdf.set_font('league', '', fix - len(name_spt[-1]) // 2)
                    pdf.set_text_color(252, 252, 252)
                    pdf.set_xy(18, 128)
                    pdf.cell(195, 45, name_spt[-1].upper(), ln=1, align='L')


            #course
            pdf.add_font('OpenSans', '',
                         r'H:\vaibhav\PycharmProjects\Automation_pdf _database\Font\open\OpenSans-Bold.ttf', uni=True)
            pdf.set_font('OpenSans', '', 15)
            pdf.set_text_color(252, 252, 252)
            course_spt=data7.split(',')
            start=165
            for i in range(len(course_spt)):
                pdf.set_xy(18, start)
                pdf.cell(195, 10, course_spt[i-1].capitalize(), ln=1, align='L')
                start=start+7



            # page4
            pdf.add_page(orientation='L')
            pdf.add_font('OpenSans', '',
                         r'H:\vaibhav\PycharmProjects\Automation_pdf _database\Font\open\OpenSans-Bold.ttf', uni=True)
            pdf.set_font('OpenSans', '', 34)
            pdf.set_text_color(0, 74, 173)
            # back ground
            # pdf.image(r'background/images.jpg', x = 0, y = 0, w = 3508, h = 2480)
            pdf.image(r'background/side_cover.jpg', x=0, y=0, w=297, h=210)

            # txt = 'Mr. vaibhav rokde'
            pdf.set_xy(10, 22)
            pdf.cell(0, 35, data8, ln=1, align='C')

            pdf.add_font('OpenSans', '',
                         r'H:\vaibhav\PycharmProjects\Automation_pdf _database\Font\open\OpenSans-Light.ttf', uni=True)

            pdf.set_font('OpenSans', '', 16)
            pdf.set_text_color(0, 0, 0)
            pdf.set_xy(25, 86)
            pdf.cell(120, 16, data8, ln=1, align='C')

            '''pdf.add_font('OpenSans', '',
                         r'H:\vaibhav\PycharmProjects\Automation_pdf _database\Font\open\OpenSans-Regular.ttf', uni=True)
            pdf.set_font('OpenSans', '', 11)#OpenSans-Regular'''

            pdf.set_font('Arial', '', 11)
            pdf.set_text_color(25, 25, 25)
            test_spt=data9.split(',')
            start = 95
            for i in range(len(test_spt)):
                pdf.set_xy(25, start)
                pdf.cell(120, 10, course_spt[i - 1].capitalize(), ln=1, align='C')
                start = start + 5



            d = str(self.date)
            d = d.replace('/', '')
            d = d + str(self.time)
            d = d.replace(':', '')

            pdf.output(r'C:/Users/admin/Downloads/{data1}PDF_Doc_{d}.pdf'.format(data1=data1,d=d))


            self.add['bg'] = 'light green'
            self.add['text'] = 'Done !'

            print('Available')

        else:
            self.add['bg']='red'
            self.add['text'] = 'try again'
        pass

    def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        set_text = f" {self.time} \n {self.date}"
        self.date_time.configure(text=set_text, font=("", 13, "bold"), bd=0, bg="white", fg="black")
        self.date_time.after(100, self.show_time)

    def Exit(self):
        self.window.destroy()

    def show_frame(self, frame):
        frame.tkraise()






def win():


    #cnx = sqlite3.connect('test_database')
    #data = pd.read_sql('select * from data1', cnx)
    #print(data.columns)
    #cnx.commit()
    #cnx.close()

    cnx = sqlite3.connect('student_database')
    data_all = pd.read_sql('select * from ipat_data', cnx)
    print(data_all.columns)
    cnx.commit()
    cnx.close()


    window = Tk()
    Dashboard(window,data_all)#, data)
    window.mainloop()

if __name__ =='__main__':

    win()

