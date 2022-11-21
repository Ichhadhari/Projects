################################################ import libraries #################################################
from tkinter import *
import tkinter as tk
# import filedialog module
from tkinter import filedialog
import pandas as pd
import numpy as np



################################################# FUNCTION AREA ################################################
# file explorer window
def browse_email_Files():
    filename = filedialog.askopenfilename(initialdir="/",title="Select a File",filetypes=(("Text files", "*.xlsx*"),("all files","*.*")))

    # Change file contents
    E1_file.set(filename)


def browse_Folder():
    filename = filedialog.askdirectory()
    # Change file contents
    E2_file.set(filename)

def exit_here():
    window.destroy()

def reset_all():
    E1_file.set('')
    E2_file.set('')
    stage_label['bg'] = '#dff2f2'
    stage_label['text'] = 'Entry stage'

def family_map():
    file_name=E1_file.get()
    voter_data = pd.read_excel(file_name)
    voter_data['father full name'] = voter_data['RLN_FM_NM_EN'] + ' ' + voter_data['RLN_L_NM_EN']
    voter_data['voter name'] = voter_data['FM_NAME_EN'] + ' ' + voter_data['LASTNAME_EN']
    voter_data = voter_data.astype(str)
    voter_data['length_address'] = voter_data['C_HOUSE_NO'].str.len()
    # voter_data=voter_data[voter_data['length_address']>4]
    voter_data['length_name'] = voter_data['father full name'].str.split().str.len()
    voter_data = voter_data[voter_data['length_name'] > 1]
    gp = voter_data.groupby(['father full name', 'C_HOUSE_NO', 'voter name'])
    data = pd.DataFrame(gp.first())
    data = data.reset_index()
    data['family group'] = data.groupby(['father full name', 'C_HOUSE_NO']).ngroup()
    family_values = data['family group'].value_counts().to_frame()
    single = family_values[family_values['family group'] == 1]
    data['father full name'] = data['father full name'].astype(str)

    data['Father name data add'] = ''
    for i in range(len(single)):
        check = single.index[i]
        name_list = []
        info = data[data['family group'] == check]
        Name = info.iloc[0, 2]
        address = info.iloc[0, 1]
        name_list = Name.split(' ')
        name_list = list(filter(None, name_list))
        Name = ' '.join(name_list).lower()
        age = int(info.iloc[0, 9])
        print(Name, age)
        for j in range(len(data)):
            value_check_with = data.iloc[j, 0]
            value_add = data.iloc[j, 1]
            value_check_with = str(value_check_with)
            value_check_with_lst = []
            min_f = value_check_with
            value_check_with_lst = value_check_with.split(' ')
            F_name = ' '.join(value_check_with_lst).lower()
            value_age = data.iloc[j, 9]
            if value_add != '' and value_add != 'nan':
                if F_name == Name and (float(value_age) <= float(age - 10)) and (address == value_add):
                    data = Insert_row(j + 1, data, info.iloc[0, :])
                    data.iloc[j + 1, -1] = 'Father name in group added'
                    data.iloc[j + 1, -2] = data.iloc[j, -2]
                    print(data.iloc[j + 1, -1], j)
                    delete_index = data[data['family group'] == check].index
                    data.drop(delete_index, inplace=True)

        data.to_excel('{}/Family Data.xlsx'.format(E2_file.get()))
        stage_label['bg'] = 'light green'
        stage_label['text'] = 'Done'

    # Function to insert row in the dataframe
def Insert_row(row_number, df, row_value):
        # Starting value of upper half
        start_upper = 0

     # End value of upper half
        end_upper = row_number

        # Start value of lower half
        start_lower = row_number

        # End value of lower half
        end_lower = df.shape[0]

        # Create a list of upper_half index
        upper_half = [*range(start_upper, end_upper, 1)]

        # Create a list of lower_half index
        lower_half = [*range(start_lower, end_lower, 1)]

        # Increment the value of lower half by 1
        lower_half = [x.__add__(1) for x in lower_half]

        # Combine the two lists
        index_ = upper_half + lower_half

        # Update the index of the dataframe
        df.index = index_

        # Insert a row at the end
        df.loc[row_number] = row_value

        # Sort the index labels
        df = df.sort_index()

        # return the dataframe
        return df

########################################################## Create the root window display ##########################################
window = Tk()
E1_file=StringVar()
E2_file=StringVar()

# Set window title
window.title('Family Mapping')
# Set window size
window.geometry("400x400")
# Set window background color
window.config(background="#dff2f2")
# Create a Family Mapping label
label_file_explorer = Label(window,text="Family Mapping",fg="black",font=('calibre',13, 'bold'))
label_file_explorer.place(x=1, y=50,height=20, width=399)

################################## Input excel for mapping
button_explore1 = Button(window,text="Input Excel",command=browse_email_Files)
button_explore1.place(x=300, y=140,height=20, width=80)

E1 = Entry(window,textvariable = E1_file, bd=1)
E1.place(x=10, y=140,height=20, width=280)


################################## Input folder for mapping
button_explore2 = Button(window,text="Output Folder",command=browse_Folder)
button_explore2.place(x=300, y=180,height=20, width=80)

E2 = Entry(window,textvariable = E2_file, bd=1)
E2.place(x=10, y=180,height=20, width=280)



start =  Button(window,text="Start Mapping",bg='red',command=family_map)
start.place(x=125, y=220,height=30, width=150)

# creating a state
stage_label = tk.Label(window, text='Entry stage',bg='#dff2f2', font=('calibre', 10, 'bold'))
stage_label.place(x=150, y=300,height=30, width=100)

update_label = tk.Label(window, text='updated here',bg='#dff2f2', font=('calibre', 10))
update_label.place(x=100, y=265,height=30, width=200)

reset_b =  Button(window,text="R",bg='red',bd=2,command=reset_all)
reset_b.place(x=10, y=2,height=18, width=30)

my_label = tk.Label(window, text='by vaibhav',bg='#dff2f2', font=('Segoe Script', 6))
my_label.place(x=300, y=390,height=10, width=50)


button_exit = Button(window,text="Exit",command=exit_here)
button_exit.place(x=170, y=350,height=20, width=60)



# Let the window wait for any events
window.mainloop()





