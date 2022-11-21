from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox

from PIL import ImageTk, Image
from datetime import *
import time
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from pandastable import Table, TableModel
import sqlite3



class Dashboard:
    def __init__(self, window, data):
        self.data=data
        self.window = window
        self.window.title('System Management Dashboard')
        self.window.geometry('1200x750')
        self.window.state('zoomed')
        self.window.resizable(0, 0)
        self.window.config(background='#eff5f6')
        self.sidebar = Frame(self.window, bg='#ffffff')
        self.sidebar.place(x=0, y=0, width=200, height=750)

        # Name of brand/person
        self.brandName = Label(self.sidebar, text='Master', bg='#ffffff', font=("", 15, "bold"))
        self.brandName.place(x=70, y=100)

        # Dashboard
        self.dashboard_text = Button(self.sidebar, text='>Dashboard', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                     cursor='hand2', activebackground='#ffffff',command=lambda: self.show_frame(self.frame1))
        self.dashboard_text.place(x=45, y=190)

        #Filter

        self.manage_text = Button(self.sidebar, text='>Filter Data', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff',command=lambda: self.show_frame(self.frame2))
        self.manage_text.place(x=45, y=220)

        #add activity
        self.activity_text = Button(self.sidebar, text='>Add Activity Data', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff',
                                  command=lambda: self.show_frame(self.frame4))
        self.activity_text.place(x=45, y=250)

        #EXIT
        self.exit_text = Button(self.sidebar, text='>Exit', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff', command=self.Exit)
        self.exit_text.place(x=45, y=280)
        # ======= TIME AND DATE ============

        self.date_time = Label(self.window)
        self.date_time.place(x=50, y=15)
        self.show_time()

        #name

        self.header = Frame(self.sidebar, bg='#009df4')
        self.header.place(x=0, y=500, width=300, height=25)
        self.heading = Label(self.sidebar, text='Data Analysis GUI', font=("", 13, "bold"), fg='#0064d3', bg='#eff5f6')
        self.heading.place(x=20, y=500)

        #======================== Body Frames ==========================

        self.frame1 = Frame(self.window, bg='light blue')
        #self.frame1.place(x=220, y=1, width=750, height=800)

        self.frame2 = Frame(self.window, bg='white')
        #self.frame2.place(x=220, y=1, width=750, height=800)

        self.frame4 = Frame(self.window, bg='light blue')

        self.frame3 = Frame(self.window, bg='yellow')
        #self.frame3.place(x=220, y=1, width=750, height=800)

        for frame in (self.frame1, self.frame2,self.frame4 , self.frame3):
            frame.place(x=200, y=1, width=1100, height=900)



        ####################################################### frame 1 subframe ###########################

        graph_frame1=Frame(self.frame1, bg='white', bd=2)
        graph_frame1.place(x=1, y=1, width=600, height=400)

        graph_frame2 = Frame(self.frame1, bg='white')
        graph_frame2.place(x=605, y=1, width=420, height=400)

        self.graph_frame3 = Frame(self.frame1, bg='white')
        self.graph_frame3.place(x=1, y=450, width=300, height=400)

        self.graph_frame4 = Frame(self.frame1, bg='white')
        self.graph_frame4.place(x=305, y=450, width=305, height=400)

        self.graph_frame5 = Frame(self.frame1, bg='white')
        self.graph_frame5.place(x=615, y=450, width=250, height=400)

        self.graph_frame6 = Frame(self.frame1, bg='white')
        self.graph_frame6.place(x=875, y=450, width=305, height=400)



        ###################################Frame editing############################
        self.g_graph = Button(self.frame1, text='Generate Dashboard',font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff', command=self.graph)
        self.g_graph.place(x=650, y=410)

        # first option
        self.a1_clicked = StringVar()
        self.a1_clicked.set('All')

        self.a1 = OptionMenu(self.frame1, self.a1_clicked, "M", "F", "T", "All")
        self.a1.place(x=75, y=410,height=20)

        self.q1 = Label(self.frame1, text='Gender:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
        self.q1.place(x=20, y=410,height=20)

        # second option
        self.a2_clicked = StringVar()
        self.a2_clicked.set('All')

        self.a2 = Combobox(self.frame1, textvariable=self.a2_clicked,values=[ 'All','18','19','20','21', '22', '23', '24', '25', '26', '27','28','29','30',
                                '31', '32', '33', '34', '35', '36', '37','38','39','40','41', '42', '43', '44', '45', '46', '47','48','49','50','51', '52', '53', '54', '55', '56', '57','58','59','60','61', '62', '63', '64', '65', '66', '67','68','69','70',
                                '71', '72', '73', '74', '75', '76', '77','78','79','80','81', '82', '83', '84', '85', '86', '87','88','89','90','91', '92', '93', '94', '95', '96', '97','98','99','100',
                             '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116','117', '118', '119', '120']

                             )
        self.a2.place(x=180, y=410, height=20, width=50)

        self.q2 = Label(self.frame1, text='Age:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
        self.q2.place(x=145, y=410, height=20)

        '''# fourth option

        self.a4_clicked = StringVar()
        self.a4_clicked.set('All')

        self.a4 = OptionMenu(self.frame1, self.a4_clicked, 'single', '2', '3', '4', '5','6','Big family')
        self.a4.place(x=465, y=410, height=20)

        self.q4 = Label(self.frame1, text='Family Count:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
        self.q4.place(x=380, y=410, height=20)'''


        # third option
        self.a3_clicked = StringVar()
        self.a3_clicked.set('All')

        self.a3 = OptionMenu(self.frame1, self.a3_clicked, 'Available','Not_Available','All')
        self.a3.place(x=300, y=410, height=20)

        self.q3 = Label(self.frame1, text='Mobile:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
        self.q3.place(x=250, y=410, height=20)

        # fourth option

        self.a4_clicked = StringVar()
        self.a4_clicked.set('All')

        self.a4 = Combobox(self.frame1, textvariable=self.a4_clicked,values=[ 'All','1', '2', '3', '4', '5', '6', '7','8','9','10','11', '12', '13', '14', '15', '16', '17','18','19','20','21', '22', '23', '24', '25', '26', '27','28','29','30',
                                '31', '32', '33', '34', '35', '36', '37','38','39','40','41', '42', '43', '44', '45', '46', '47','48','49','50','51', '52', '53', '54', '55', '56', '57','58','59','60','61', '62', '63', '64', '65', '66', '67','68','69','70',
                                '71', '72', '73', '74', '75', '76', '77','78','79','80','81', '82', '83', '84', '85', '86', '87','88','89','90','91', '92', '93', '94', '95', '96', '97','98','99','100',
                             '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116','117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130',
                             '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145',
                             '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160',
                             '161', '162', '163', '164', '165', '166', '167', '168', '169', '170',
                             '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185',
                             '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199', '200',
                                '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222', '223', '224', '225', '226', '227', '228', '229', '230',
                                '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241', '242', '243', '244', '245', '246', '247', '248', '249', '250', '251', '252', '253', '254', '255', '256', '257', '258', '259', '260', '261', '262', '263', '264', '265', '266', '267', '268', '269', '270',
                                '271', '272', '273', '274', '275', '276', '277', '278', '279', '280', '281', '282', '283', '284', '285', '286', '287', '288', '289', '290', '291', '292', '293', '294', '295', '296', '297', '298', '299', '300',
                             '301', '302', '303', '304', '305', '306', '307', '308', '309', '310', '311', '312', '313', '314', '315', '316',
                             '317', '318', '319', '320', '321', '322', '323', '324', '325', '326', '327', '328', '329', '330',
                             '331', '332', '333', '334', '335', '336', '337', '338', '339', '340', '341', '342', '343', '344', '345',
                             '346', '347', '348', '349', '350', '351', '352', '353', '354', '355', '356', '357', '358', '359', '360',
                             '361', '362', '363', '364', '365', '366', '367', '368', '369', '370',
                             '371', '372', '373', '374', '375', '376', '377', '378', '379', '380', '381', '382', '383', '384', '385',
                             '386', '387', '388', '389', '390', '391', '392', '393', '394', '395', '396', '397', '398', '399', '400',
                             '401', '402', '403', '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415', '416',
                             '417', '418', '419', '420', '421', '422', '423', '424', '425', '426', '427', '428', '429', '430',
                             '431', '432', '433', '434', '435', '436', '437', '438', '439', '440', '441', '442', '443', '444', '445',
                             '446', '447', '448', '449', '450', '451', '452', '453', '454', '455', '456', '457', '458', '459', '460',
                             '461', '462', '463', '464', '465', '466', '467', '468', '469', '470',
                             '471', '472', '473', '474', '475', '476', '477', '478', '479', '480', '481', '482', '483', '484', '485',
                             '486', '487', '488', '489', '490', '491', '492', '493', '494', '495', '496', '497', '498', '499', '500']

                             )
        self.a4.place(x=465, y=410, height=20,width=70)

        self.q4 = Label(self.frame1, text='Port_No:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
        self.q4.place(x=380, y=410, height=20)

        ####################################################### frame 2 subframe ###########################

        #self.frame2 = Frame(self.window, bg='black')

        self.F1_clicked = StringVar()
        self.F1_clicked.set('FILTER/SEARCH')

        self.f1 = OptionMenu(self.frame2, self.F1_clicked, 'FILTER/SEARCH', 'ADD_DATA')
        self.f1.place(x=300, y=20, height=30, width=150)

        self.Filter_op = Button(self.frame2, text='USE SERVICE', font=("", 13, "bold"), bd=0,
                              cursor='hand2', activebackground='#ffffff', command=self.filter)
        self.Filter_op.place(x=500, y=20,height=30, width=200)

        self.f_frame1 = Frame(self.frame2, bg='white')
        self.f_frame2 = Frame(self.frame2, bg='white')


        ###### frame 4 subfeame

        Add_label=Button(self.frame4, text='Browse adding file:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6',command=self.open_Activity_file)
        Add_label.place(x=200, y=100, height=30, width=150)

        self.Add_entry = Entry(self.frame4,bd=2)
        self.Add_entry.place(x=400, y=100, height=30, width=300)

        Add_data = Button(self.frame4, text='Add activity', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6',
                           command=self.add_activity)
        Add_data.place(x=300, y=180, height=30, width=150)

        self.template_b = Button(self.frame4, text='TEMPLATE EXCEL', font=("", 9, "bold"), fg='#0064d3', bg='light blue',
                          command=self.template)
        self.template_b.place(x=900, y=100, height=28, width=120)






        window.mainloop()





    ########################################################################function@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

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

    def open_Activity_file(self):
        print("it's working")
        A_file = askopenfilename(parent=self.frame4, title='Choose the file', filetypes=[("excel file", "*.xlsx")])
        self.Add_entry.insert(0, A_file)

    def template(self):
        temp={
            'name':[''],
            'surname': [''],
            'mobile':[''],
            'activity':['']
        }
        temp_df=pd.DataFrame.from_dict(temp)
        d = str(self.date)
        d = d.replace('/', '')
        d = d + str(self.time)
        d = d.replace(':', '')
        temp_df.to_excel(r"C:/Users/admin/Downloads/activity_template_{d}.xlsx".format(d=d), index=False)
        self.template_b['bg'] = 'light green'
        pass

    def add_activity(self):
        activity_file=self.Add_entry.get()
        if (activity_file != '') & (activity_file[-5:]=='.xlsx'):
            maindata=self.data
            activity_data = pd.read_excel(activity_file)
            print(activity_data)
            conn = sqlite3.connect('test_database')
            # Create cursor.
            c = conn.cursor()
            activity_data['epic_number'] = ''
            print('checking')
            for i in range(len(activity_data)):
                person = ''
                person = str(activity_data.iloc[i, 2])
                activity_box = str(activity_data.iloc[i, 3])
                person = person.replace(' ', '').replace('+', '').replace('_', '')
                if person[-2:]=='.0':
                    del person[-2:]
                if person != '':
                    person = str(person[-10:])
                    print(person)

                    for j in range(len(maindata)):
                        data_person = ''
                        all_no = []
                        data_person = str(maindata.iloc[j, 20])
                        if data_person != '':
                            all_no = data_person.split('#')
                            print(all_no)
                            for k in all_no:
                                if k[-2:] == '.0':
                                    del k[-2:]
                                k = k[-10:]
                                if k == person:
                                    print('detect')
                                    maindata.iloc[j, -1] = maindata.iloc[j, -1]+','+activity_box
                                    activity_data.iloc[i, -1] = maindata.iloc[j, 8]
                                    c.execute("""UPDATE data1
                                                SET Activity = :d1
                                                WHERE MOBILE_NO = :d2;""",
                                              {
                                                  'd1': maindata.iloc[j, -1],
                                                  'd2':person
                                              })

                                else:
                                    pass




                else:
                    pass
            d = str(self.date)
            d = d.replace('/', '')
            d = d + str(self.time)
            d = d.replace(':', '')
            activity_data.to_excel(r"C:/Users/admin/Downloads/activity_data_{d}.xlsx".format(d=d), index=False)
            self.data=maindata
            print(self.data)
            self.Add_entry.delete(0, END)
            # Commit Changes
            conn.commit()
            # Close Connection
            conn.close()

            print('done')

        pass


    def filter(self):
        f_selection=a1 = self.F1_clicked.get()
        if f_selection=='FILTER/SEARCH':


            self.f_frame1.place(x=50, y=80, width=1000, height=800)

            ################          option ###################################

            self.SEARCH = Button(self.f_frame1, text='Search', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#00ffff', command=self.Search_operation)
            self.SEARCH.place(x=300, y=40, height=20)

            self.SEARCH1 = Button(self.f_frame1, text='Filter', font=("", 13, "bold"), bd=0,
                                 cursor='hand2', activebackground='#00ffff', command=self.filter_operation)
            self.SEARCH1.place(x=650, y=10)

            # first option
            self.s1_clicked = StringVar()
            self.s1_clicked.set('All')

            self.s1 = OptionMenu(self.f_frame1, self.s1_clicked, "M", "F", "T", "All")
            self.s1.place(x=75, y=10, height=20)

            self.ss1 = Label(self.f_frame1, text='Gender:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
            self.ss1.place(x=20, y=10, height=20)

            # second option
            self.s2_clicked = StringVar()
            self.s2_clicked.set('All')

            self.s2 = OptionMenu(self.f_frame1, self.s2_clicked, 'first time V', '21 to 25', '25 to 30', '31 to 35',
                                 '36 to 40', '41 to 45', '46 to 50', '51 to 55', '55 to 60', 'senior citien', 'All')
            self.s2.place(x=180, y=10, height=20)

            self.ss2 = Label(self.f_frame1, text='Age:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
            self.ss2.place(x=145, y=10, height=20)

            '''# fourth option

            self.a4_clicked = StringVar()
            self.a4_clicked.set('All')

            self.a4 = OptionMenu(self.frame1, self.a4_clicked, 'single', '2', '3', '4', '5','6','Big family')
            self.a4.place(x=465, y=410, height=20)

            self.q4 = Label(self.frame1, text='Family Count:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
            self.q4.place(x=380, y=410, height=20)'''

            # third option
            self.s3_clicked = StringVar()
            self.s3_clicked.set('All')

            self.s3 = OptionMenu(self.f_frame1, self.s3_clicked, 'Available', 'Not_Available', 'All')
            self.s3.place(x=300, y=10, height=20)

            self.ss3 = Label(self.f_frame1, text='Mobile:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
            self.ss3.place(x=250, y=10, height=20)

            # fourth option

            self.s4_clicked = StringVar()
            self.s4_clicked.set('All')

            self.s4 = Combobox(self.f_frame1, textvariable=self.s4_clicked,
                               values=['All', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                                       '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                                       '28', '29', '30',
                                       '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43',
                                       '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56',
                                       '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69',
                                       '70',
                                       '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83',
                                       '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96',
                                       '97', '98', '99', '100',
                                       '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111',
                                       '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122',
                                       '123', '124', '125', '126', '127', '128', '129', '130',
                                       '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141',
                                       '142', '143', '144', '145',
                                       '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156',
                                       '157', '158', '159', '160',
                                       '161', '162', '163', '164', '165', '166', '167', '168', '169', '170',
                                       '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181',
                                       '182', '183', '184', '185',
                                       '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196',
                                       '197', '198', '199', '200',
                                       '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211',
                                       '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222',
                                       '223', '224', '225', '226', '227', '228', '229', '230',
                                       '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241',
                                       '242', '243', '244', '245', '246', '247', '248', '249', '250', '251', '252',
                                       '253', '254', '255', '256', '257', '258', '259', '260', '261', '262', '263',
                                       '264', '265', '266', '267', '268', '269', '270',
                                       '271', '272', '273', '274', '275', '276', '277', '278', '279', '280', '281',
                                       '282', '283', '284', '285', '286', '287', '288', '289', '290', '291', '292',
                                       '293', '294', '295', '296', '297', '298', '299', '300',
                                       '301', '302', '303', '304', '305', '306', '307', '308', '309', '310', '311',
                                       '312', '313', '314', '315', '316',
                                       '317', '318', '319', '320', '321', '322', '323', '324', '325', '326', '327',
                                       '328', '329', '330',
                                       '331', '332', '333', '334', '335', '336', '337', '338', '339', '340', '341',
                                       '342', '343', '344', '345',
                                       '346', '347', '348', '349', '350', '351', '352', '353', '354', '355', '356',
                                       '357', '358', '359', '360',
                                       '361', '362', '363', '364', '365', '366', '367', '368', '369', '370',
                                       '371', '372', '373', '374', '375', '376', '377', '378', '379', '380', '381',
                                       '382', '383', '384', '385',
                                       '386', '387', '388', '389', '390', '391', '392', '393', '394', '395', '396',
                                       '397', '398', '399', '400',
                                       '401', '402', '403', '404', '405', '406', '407', '408', '409', '410', '411',
                                       '412', '413', '414', '415', '416',
                                       '417', '418', '419', '420', '421', '422', '423', '424', '425', '426', '427',
                                       '428', '429', '430',
                                       '431', '432', '433', '434', '435', '436', '437', '438', '439', '440', '441',
                                       '442', '443', '444', '445',
                                       '446', '447', '448', '449', '450', '451', '452', '453', '454', '455', '456',
                                       '457', '458', '459', '460',
                                       '461', '462', '463', '464', '465', '466', '467', '468', '469', '470',
                                       '471', '472', '473', '474', '475', '476', '477', '478', '479', '480', '481',
                                       '482', '483', '484', '485',
                                       '486', '487', '488', '489', '490', '491', '492', '493', '494', '495', '496',
                                       '497', '498', '499', '500']

                               )
            self.s4.place(x=465, y=10, height=20)

            self.ss4 = Label(self.f_frame1, text='Port_No:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
            self.ss4.place(x=380, y=10, height=20)
            ## mobile number

            self.s5_clicked = StringVar()
            self.s5_clicked.set('All')
            self.s5 = Combobox(self.f_frame1, textvariable=self.s5_clicked,
                               values=['All'])
            self.s5.place(x=130, y=40, height=20)

            self.ss5 = Label(self.f_frame1, text='Mobile No:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
            self.ss5.place(x=20, y=40, height=20)



        elif f_selection=='ADD_DATA':
            self.f_frame2.place(x=50, y=80, width=1000, height=800)

            self.name=StringVar()
            self.F_name = StringVar()
            self.house_no=StringVar()
            self.part_no=StringVar()
            self.epic_no=StringVar()
            self.age=StringVar()
            self.gender=StringVar()
            self.mobile_no=StringVar()
            self.family_group=StringVar()

            add_label1=Label(self.f_frame2, text='Voter Name:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
            add_label1.place(x=70, y=40, height=20)
            self.add_label1_E1=Entry(self.f_frame2,textvariable = self.name, font=('calibre',10,'normal'))
            self.add_label1_E1.place(x=300, y=40, height=20)


            add_label2 = Label(self.f_frame2, text='Father Name:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
            add_label2.place(x=70, y=70, height=20)
            add_label2_E2 = Entry(self.f_frame2, textvariable=self.F_name, font=('calibre', 10, 'normal'))
            add_label2_E2.place(x=300, y=70, height=20)

            add_label3 = Label(self.f_frame2, text='House_No:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
            add_label3.place(x=70, y=100, height=20)
            add_label3_E3 = Entry(self.f_frame2, textvariable=self.house_no, font=('calibre', 10, 'normal'))
            add_label3_E3.place(x=300, y=100, height=20)

            add_label4 = Label(self.f_frame2, text='part_no:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
            add_label4.place(x=70, y=130, height=20)#part_no
            add_label4_E4 = Entry(self.f_frame2, textvariable=self.part_no, font=('calibre', 10, 'normal'))
            add_label4_E4.place(x=300, y=130, height=20)

            add_label5 = Label(self.f_frame2, text='epic_no:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
            add_label5.place(x=70, y=160, height=20)
            add_label5_E5 = Entry(self.f_frame2, textvariable=self.epic_no, font=('calibre', 10, 'normal'))
            add_label5_E5.place(x=300, y=160, height=20)

            add_label6 = Label(self.f_frame2, text='age:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
            add_label6.place(x=70, y=190, height=20)
            add_label6_E6 = Entry(self.f_frame2, textvariable=self.age, font=('calibre', 10, 'normal'))
            add_label6_E6.place(x=300, y=190, height=20)

            add_label7 = Label(self.f_frame2, text='gender:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
            add_label7.place(x=70, y=220, height=20)
            add_label7_E7 = Entry(self.f_frame2, textvariable=self.gender, font=('calibre', 10, 'normal'))
            add_label7_E7.place(x=300, y=220, height=20)

            add_label8 = Label(self.f_frame2, text='Mobile_no:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
            add_label8.place(x=70, y=250, height=20)
            add_label8_E8 = Entry(self.f_frame2, textvariable=self.mobile_no, font=('calibre', 10, 'normal'))
            add_label8_E8.place(x=300, y=250, height=20)

            add_label9 = Label(self.f_frame2, text='family_group:', font=("", 9, "bold"), fg='#0064d3', bg='#eff5f6')
            add_label9.place(x=70, y=280, height=20)
            add_label9_E9 = Entry(self.f_frame2, textvariable=self.family_group, font=('calibre', 10, 'normal'))
            add_label9_E9.place(x=300, y=280, height=20)

            self.add=Button(self.frame2, text='ADD', font=("", 13, "bold"), bd=0,
                              cursor='hand2', activebackground='#ffffff', command=self.add_row)
            self.add.place(x=250, y=450, width=80 , height=30)

            self.re = Button(self.frame2, text='Reset', font=("", 10, "bold"), bd=0,
                              cursor='hand2', activebackground='#ffffff', command=self.reset)
            self.re.place(x=750, y=50, width=80, height=30)






    def reset(self):
        print('here')
        self.add['bg'] = '#eff5f6'
        self.name.set('')
        self.F_name.set('')
        self.house_no.set('')
        self.part_no.set('')
        self.epic_no.set('')
        self.age.set('')
        self.gender.set('')
        self.mobile_no.set('')
        self.family_group.set('')


    def add_row(self):
        if ( self.name.get() != '') & (self.mobile_no.get() != ''):

            conn = sqlite3.connect('test_database')
            # Create cursor.
            c=conn.cursor()
            # Create table
            c.execute("""INSERT INTO data1 VALUES (:v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8, :v9, :v10, :v11, :v12, :v13, :v14, :v15, :v16, :v17, :v18, :v19, :v20, :v21, :v22, :v23, :v24, :v25, :v26, :v27,:v28,:v29,:v30)""",
                      {
                          'v1':len(self.data) ,
                          'v2':self.F_name.get(),
                          'v3':self.house_no.get(),
                          'v4':self.name.get(),
                          'v5':'',
                          'v6':self.part_no.get(),
                          'v7':'',
                          'v8': '',
                          'v9': self.epic_no.get(),
                          'v10': self.gender.get(),
                          'v11': self.age.get(),
                          'v12':'',
                          'v13': '',
                          'v14': '',
                          'v15': '',
                          'v16': '',
                          'v17': '',
                          'v18': '',
                          'v19': '',
                          'v20': '',
                          'v21': self.mobile_no.get(),
                          'v22': '',
                          'v23': '',
                          'v24': '',
                          'v25': '',
                          'v26': '',
                          'v27': self.family_group.get(),
                          'v28':'Added by you',
                          'v29':'Added by you',
                          'v30':''
                      }
                      )
            # Commit Changes
            conn.commit()
            # Close Connection
            conn.close()




            self.add['bg']='light green'
            self.name.set('')
            self.F_name.set('')
            self.house_no.set('')
            self.part_no.set('')
            self.epic_no.set('')
            self.age.set('')
            self.gender.set('')
            self.mobile_no.set('')
            self.family_group.set('')

        else:
            self.add['bg'] = 'red'
            self.add['text'] = 'Try Again!'

        pass

    def filter_operation(self):
        s1 = self.s1_clicked.get()
        s2 = self.s2_clicked.get()
        s3 = self.s3_clicked.get()
        s4 = self.s4_clicked.get()
        if s4 != 'All':
            s4 = int(s4)

        print(s1, s2, s3, s4)
        if (s1 == 'All') & (s2 == 'All') & (s3 == 'All') & (s4 == 'All'):
            self.filter_output = self.data

        elif (s1 == 'All') & (s2 == 'All') & (s3 == 'All') & (s4 != 'All'):
            self.filter_output = self.data[self.data.PART_NO == s4]

        elif (s1 == 'All') & (s2 == 'All') & (s3 != 'All')& (s4 == 'All'):
            self.filter_output = self.data[self.data.mobile_available == s3]

        elif (s1 == 'All') & (s2 != 'All') & (s3 == 'All')& (s4 == 'All'):
            self.filter_output = self.data[self.data.Age_Between == s2]

        elif (s1 != 'All') & (s2 == 'All') & (s3 == 'All')& (s4 == 'All'):
            self.filter_output = self.data[self.data.GENDER.str.contains(s1)]

        elif (s1 != 'All') & (s2 != 'All') & (s3 == 'All')& (s4 == 'All'):
            self.filter_output = self.data[(self.data.GENDER.str.contains(s1)) & (self.data.Age_Between == s2)]

        elif (s1 == 'All') & (s2 != 'All') & (s3 != 'All')& (s4 == 'All'):
            self.filter_output = self.data[(self.data.Age_Between == s2) & (self.data.mobile_available == s3)]

        elif (s1 == 'All') & (s2 == 'All') & (s3 != 'All')& (s4 != 'All'):
            self.filter_output = self.data[(self.data.PART_NO == s4) & (self.data.mobile_available == s3)]

        elif (s1 != 'All') & (s2 == 'All') & (s3 == 'All')& (s4 != 'All'):
            self.filter_output = self.data[(self.data.PART_NO == s4) & self.data.GENDER.str.contains(s1)]

        elif (s1 == 'All') & (s2 != 'All') & (s3 == 'All')& (s4 != 'All'):
            self.filter_output = self.data[(self.data.PART_NO == s4) & self.data.Age_Between == s2]

        elif (s1 != 'All') & (s2 == 'All') & (s3 != 'All') & (s4 == 'All'):
            self.filter_output = self.data[(self.data.GENDER.str.contains(s1)) & (self.data.mobile_available == s3)]

        elif (s1 != 'All') & (s2 != 'All') & (s3 != 'All') & (s4 != 'All'):
            self.filter_output = self.data[(self.data.GENDER.str.contains(s1)) & (self.data.Age_Between == s2) & (
                        self.data.mobile_available == s3) & (self.data.PART_NO == s4)]


        print(self.filter_output.head())
        self.Filter_subframe = Frame(self.f_frame1, bg='red')
        self.Filter_subframe.place(x=2, y=70, width=1000, height=700)




        self.table = pt = Table(self.Filter_subframe, dataframe=self.filter_output, showtoolbar=True, showstatusbar=True)
        pt.show()

        self.Export = Button(self.f_frame1, text='Export', font=("", 13, "bold"), bd=0,bg='light blue',
                              cursor='hand2', activebackground='#00ffff', command=self.export)
        self.Export.place(x=650, y=40)

        pass

    def export(self):
        print('output in Downloads folder')
        d=str(self.date)
        d=d.replace('/','')
        d=d+str(self.time)
        d=d.replace(':','')
        print(self.filter_output.head())
        self.filter_output.to_csv(r"C:/Users/admin/Downloads/output_{d}.csv".format(d=d), index=False)
        self.Export['bg']='light green'


    def Search_operation(self):
        self.Filter_subframe = Frame(self.f_frame1, bg='red')
        self.Filter_subframe.place(x=2, y=70, width=1000, height=700)

        mob_contact = self.s5_clicked.get()

        if mob_contact == 'All':
            self.table = pt = Table(self.Filter_subframe, dataframe=self.data, showtoolbar=True, showstatusbar=True)
            pt.show()

        else:
            mob_contact = mob_contact.replace('+', '').replace(' ', '').replace('_', '')

            self.contact_search = self.data[self.data.MOBILE_NO.str.contains(mob_contact)]
            self.table = pt = Table(self.Filter_subframe, dataframe=self.contact_search, showtoolbar=True,
                                    showstatusbar=True)
            pt.show()


    def graph(self):
        a1 = self.a1_clicked.get()
        a2 = self.a2_clicked.get()
        a3 = self.a3_clicked.get()
        a4 = self.a4_clicked.get()
        if a4 != 'All':
            a4=int(a4)

        if a2 != 'All':
            a2=int(a2)

        print(a1, a2, a3, a4)



        if (a1 == 'All') & (a2 == 'All') & (a3 == 'All') & (a4 == 'All'):
            self.output = self.data

        elif (a1 == 'All') & (a2 == 'All') & (a3 == 'All') & (a4 != 'All'):
            self.output = self.data[self.data.PART_NO == a4]

        elif (a1 == 'All') & (a2 == 'All') & (a3 != 'All')& (a4 == 'All'):
            self.output = self.data[self.data.mobile_available == a3]

        elif (a1 == 'All') & (a2 != 'All') & (a3 == 'All')& (a4 == 'All'):
            self.output = self.data[self.data.AGE == a2]

        elif (a1 != 'All') & (a2 == 'All') & (a3 == 'All')& (a4 == 'All'):
            self.output = self.data[self.data.GENDER.str.contains(a1)]

        elif (a1 != 'All') & (a2 != 'All') & (a3 == 'All')& (a4 == 'All'):
            self.output = self.data[(self.data.GENDER.str.contains(a1)) & (self.data.AGE == a2)]

        elif (a1 == 'All') & (a2 != 'All') & (a3 != 'All')& (a4 == 'All'):
            self.output = self.data[(self.data.AGE == a2) & (self.data.mobile_available == a3)]

        elif (a1 == 'All') & (a2 == 'All') & (a3 != 'All')& (a4 != 'All'):
            self.output = self.data[(self.data.PART_NO == a4) & (self.data.mobile_available == a3)]

        elif (a1 != 'All') & (a2 == 'All') & (a3 == 'All')& (a4 != 'All'):
            self.output = self.data[(self.data.PART_NO == a4) & self.data.GENDER.str.contains(a1)]

        elif (a1 == 'All') & (a2 != 'All') & (a3 == 'All')& (a4 != 'All'):
            self.output = self.data[(self.data.PART_NO == a4) & self.data.AGE == a2]

        elif (a1 != 'All') & (a2 == 'All') & (a3 != 'All') & (a4 == 'All'):
            self.output = self.data[(self.data.GENDER.str.contains(a1)) & (self.data.mobile_available == a3)]

        elif (a1 != 'All') & (a2 != 'All') & (a3 != 'All') & (a4 != 'All'):
            self.output = self.data[(self.data.GENDER.str.contains(a1)) & (self.data.AGE == a2) & (
                        self.data.mobile_available == a3) & (self.data.PART_NO == a4)]


        print(self.output.head())

        GENDER = self.output['GENDER'].value_counts()
        AGE_between_data = self.output['Age_Between'].value_counts()
        mobile_available = self.output['mobile_available'].value_counts()

        fig = plt.figure(figsize=(5, 5), dpi=100)
        fig.set_size_inches(5, 3.5)
        # fig = plt.figure(figsize=(5, 3.5), dpi=100)
        labels = ('MALE', 'FEMALE', 'T')
        labelpos = np.arange(len(labels))
        studentsum = self.output['GENDER'].value_counts()

        ##This section formats the piechart for output
        GENDER.plot.pie(autopct='%1.0f%%')

        plt.xlabel('Voter')
        plt.tight_layout(pad=2.2, w_pad=0.5, h_pad=0.1)
        plt.title('Gender wise Data')
        plt.xticks(rotation=30, horizontalalignment="center")
        ## This section draws a canvas to allow the barchart to appear in it
        canvasbar = FigureCanvasTkAgg(fig, master=self.frame1)
        canvasbar.draw()
        canvasbar.get_tk_widget().place(x=750, y=200, anchor=CENTER)  # show the barchart on the ouput window

        fig = plt.figure(figsize=(5, 3.5), dpi=100)
        # Data to plot
        labels = ["first time V", "21 to 25", "26 to 30",
                  "31 to 35", "36 to 40", "41 to 45", "46 to 50",
                  "51 to 55", "56 to 60", 'senior citien']
        labelpos = np.arange(len(labels))
        sizes = [AGE_between_data]
        mini_data = self.output['Age_Between'].value_counts().to_frame()
        a = mini_data.index.tolist()
        studentsum = mini_data.values.tolist()
        print(mini_data, a, studentsum)
        # colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'Orange', 'red']
        # explode = (0.2, 0, 0, 0, 0, 0)
        # plt.xticks(labelpos, labels)
        # plt.bar(a, studentsum, align='center', alpha=1.0)

        ax = AGE_between_data.plot(kind='bar')
        for p in ax.patches:
            ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

        # plt.xticks(labelpos, labels)
        plt.ylabel('Count')
        plt.xlabel('Age Catagiry')
        plt.tight_layout(pad=2.2, w_pad=0.5, h_pad=0.1)
        plt.title('Average raw mark for all subjects')
        plt.xticks(rotation=30, horizontalalignment="center")


        canvasbar = FigureCanvasTkAgg(fig, master=self.frame1)
        canvasbar.draw()
        # canvasbar.get_tk_widget().place(x=1120, y=285, anchor=CENTER)  # show the barchart on the ouput window
        canvasbar.get_tk_widget().place(x=250, y=200, anchor=CENTER)

        '''######################## text for family group ##############################

        fig = plt.figure(figsize=(4, 4), dpi=100)
        fig.set_size_inches(4, 3.5)
        # fig = plt.figure(figsize=(5, 3.5), dpi=100)
        labels = ('single', '2', '3', '4', '5','6','Big family')
        labelpos = np.arange(len(labels))
        studentsum = self.output['family group'].value_counts().to_frame()

        ##This section formats the piechart for output
        studentsum['family group'].plot.pie()

        plt.xlabel('Voter')
        plt.tight_layout(pad=2.2, w_pad=0.5, h_pad=0.1)
        plt.title('Family wise Data')
        plt.xticks(rotation=30, horizontalalignment="center")
        ## This section draws a canvas to allow the barchart to appear in it
        canvasbar = FigureCanvasTkAgg(fig, master=self.frame1)
        canvasbar.draw()
        canvasbar.get_tk_widget().place(x=900, y=700, anchor=CENTER)'''
        ##################### total people count
        self.total_people = Label(self.graph_frame6, text='Total People', bg='#009aa5', font=("", 15, "bold"))
        self.total_people.place(x=45, y=4)

        self.totalPeople_text = Label(self.graph_frame6, text=len(self.output),
                                      font=("", 25, "bold"),bg='#e1e6e2')
        self.totalPeople_text.place(x=1, y=45,width=200,height=40)

        ##################### total Gender wise count
        self.total_Gender = Label(self.graph_frame6, text='Gender count', bg='#009aa5', font=("", 15, "bold"))
        self.total_Gender.place(x=45, y=105)

        self.totalGender_text = Label(self.graph_frame6, text=self.output['GENDER'].value_counts().to_frame(),
                                      font=("", 20, "bold"),bg='#e1e6e2')
        self.totalGender_text.place(x=1, y=135,width=200,height=150)

        ##################### total Mobile wise count
        self.total_Mobile = Label(self.graph_frame5, text='Mobile', bg='#009aa5', font=("", 15, "bold"))
        self.total_Mobile.place(x=85, y=4)

        self.totalMobile_text = Label(self.graph_frame5, text=self.output['mobile_available'].value_counts().to_frame(),
                                      font=("", 10, "bold"), bg='#e1e6e2')
        self.totalMobile_text.place(x=1, y=40,width=250,height=130)

        fig_pie = plt.figure(figsize=(3, 3), dpi=100)
        fig_pie.set_size_inches(2.5, 2.5)

        self.mobile_pie=self.output['mobile_available'].replace('Available','YES').replace('Not_Available','NO').value_counts().to_frame()

        self.mobile_pie['mobile_available'].plot.pie(autopct='%1.0f%%')

        #plt.xlabel('Data Available')
        plt.tight_layout(pad=0.2, w_pad=0.1, h_pad=0.1)
        plt.title('Mobile Data Avaibilty')
        plt.xticks(rotation=30, horizontalalignment="center")
        ## This section draws a canvas to allow the barchart to appear in it
        canvaspie = FigureCanvasTkAgg(fig_pie, master=self.graph_frame5)
        canvaspie.draw()
        canvaspie.get_tk_widget().place(x=130, y=290, anchor=CENTER)


        ##################### total Age wise count
        self.total_Age = Label(self.graph_frame4, text='Age (all data count)', bg='#009aa5', font=("", 15, "bold"))
        self.total_Age.place(x=15, y=4)

        self.total_Age_text = Label(self.graph_frame4, text=self.output['Age_Between'].value_counts().to_frame(),
                                      font=("", 10, "bold"))
        self.total_Age_text.place(x=7, y=60, width=240)

        self.subframe2 = Frame(self.graph_frame4, bg='white')
        self.subframe2.place(x=2, y=40, width=300, height=350)
        values_total_port_people2 = self.output['AGE'].value_counts().to_frame()

        h2 = Scrollbar(self.subframe2, orient='horizontal')
        h2.pack(side=BOTTOM, fill=X)
        v2 = Scrollbar(self.subframe2)
        v2.pack(side=RIGHT, fill=Y)
        '''self.values_total_port_people_text = Text(self.subframe, text=values_total_port_people,
                                      font=("", 10, "bold"),wrap = NONE,xscrollcommand = h.set,yscrollcommand = v.set)'''

        self.t2 = Text(self.subframe2, wrap=NONE,
                      xscrollcommand=h2.set,
                      yscrollcommand=v2.set)

        self.t2.insert(END, values_total_port_people2)

        self.t2.pack(side=TOP, fill=X)

        h2.config(command=self.t2.xview)
        v2.config(command=self.t2.yview)

        ##################### total port wise count



        self.total_port_people = Label(self.graph_frame3, text='Family group & count', bg='#009aa5', font=("", 15, "bold"))
        self.total_port_people.place(x=15, y=4)


        self.subframe=Frame(self.graph_frame3, bg='red')
        self.subframe.place(x=2,y=40, width=300, height=350)
        values_total_port_people=self.output['PART_NO'].value_counts().to_frame()
        print(values_total_port_people)
        h = Scrollbar(self.subframe, orient='horizontal')
        h.pack(side=BOTTOM, fill=X)
        v = Scrollbar(self.subframe)
        v.pack(side=RIGHT, fill=Y)
        '''self.values_total_port_people_text = Text(self.subframe, text=values_total_port_people,
                                      font=("", 10, "bold"),wrap = NONE,xscrollcommand = h.set,yscrollcommand = v.set)'''

        self.t = Text(self.subframe, wrap=NONE,
                 xscrollcommand=h.set,
                 yscrollcommand=v.set)

        self.t.insert(END,values_total_port_people)

        self.t.pack(side=TOP, fill=X)

        h.config(command=self.t.xview)
        v.config(command=self.t.yview)
























def win():

    #data = pd.read_excel(r"test.xlsx")
    #data = pd.read_excel(r"H:\vaibhav\PycharmProjects\PythonTkinterDashboard-main\test.xlsx")
    cnx = sqlite3.connect('test_database')
    data = pd.read_sql('select * from data1', cnx)
    print(data.columns)
    cnx.commit()
    cnx.close()
    '''data['mobile_available'] = ''
    for m in range(len(data['MOBILE_NO'])):
        mobile=str(data.iloc[m,20])
        mobile=mobile.replace('NaN', '').replace(' ', '').replace('_', '').replace('nan', '').replace('+', '')
        data.iloc[m, 20]=mobile
        if len(mobile) == 10 or len(mobile) == 12 or len(mobile) == 13:
            data.iloc[m, 20]=mobile[-12:-2]
            print(len(data.iloc[m, 20]))
            if data.iloc[m, 20] != '':
                data.iloc[m, -1] = 'Available'
                print(data.iloc[m, -1])
        else:
            data.iloc[m, -1] = 'Not_Available'
            print(data.iloc[m, -1])

    print(data['MOBILE_NO'])'''
    '''data['mobile_available'] = ''
    for i in range(len(data)):
        number = str(data.iloc[i, 20])
        if len(number) == 10 or len(number) == 12 or len(number) == 13:
            if number != '':
                data.iloc[i, -1] = 'Available'

        else:
            data.iloc[i, -1] = 'Not_Available' '''
    '''print(data['mobile_available'].value_counts().to_frame())
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
            data.iloc[i, -1] = "senior citien" '''


    window = Tk()
    Dashboard(window, data)
    window.mainloop()

if __name__ =='__main__':
    plt.show()
    win()

