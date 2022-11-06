from tkinter import *
from tkinter import *
import tkinter as tk
# import filedialog module
from tkinter import filedialog
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd


# file explorer window
def browse_idpass_Files():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))

    # Change file contents
    E1_file.set(filename)

# file explorer window
def browse_email_send_to_Files():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.xlsx*"),
                                                     ("all files",
                                                      "*.*")))

    # Change file contents
    E2_file.set(filename)

def browse_subject_Files():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))

    # Change file contents
    E3_file.set(filename)

def browse_body_Files():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))

    # Change file contents
    E4_file.set(filename)

def browse_pdf_Files():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.pdf*"),
                                                     ("all files",
                                                      "*.*")))

    # Change file contents
    E5_file.set(filename)

##################################operation send mail################################


def send_mail():
    try:
        stage_label['bg']='light green'
        stage_label['text']='working'
        button_explore1['state']='disable'
        button_explore2['state'] = 'disable'
        button_explore3['state'] = 'disable'
        button_explore4['state'] = 'disable'
        button_explore5['state'] = 'disable'
        id_pass=E1_file.get()
        send_to=E2_file.get()
        subjects=E3_file.get()
        text_body=E4_file.get()
        pdf_body=E5_file.get()

        if id_pass[-4:]=='.txt':
            with open(id_pass, 'r') as n:
                IDPASS = n.readlines()
            print(IDPASS)
            sender_address = IDPASS[0]#.replace('\n','')
            print(sender_address)
            sender_pass = IDPASS[1]#.replace('\n','')
            print(sender_pass)
            if (sender_address=='') or (sender_pass==''):

                raise TypeError('type error here')
        else :
            raise TypeError('type error here')


        ######### send to

        if send_to[-5:]=='.xlsx':
            data = pd.read_excel(send_to)
            data = data.astype(str)
            print('total mails: ',len(data))
        else :
            raise TypeError('type error here')

        ####subject read
        if subjects[-4:]=='.txt':
            with open(subjects, 'r', encoding="utf8") as n:
                subject = n.readline()
            subject = subject.replace('\n','')

            if (subject==''):
                raise IndexError('type error here')
        else :
            raise TypeError('type error here')

        ########text_body
        if text_body[-4:] == '.txt':
            with open(text_body, 'r',encoding="utf8") as n:
                mail_content = n.read()

            if (mail_content == ''):
                raise IndexError('type error here')
        else:
            raise TypeError('type error here')

        #######pdf
        if pdf_body[-4:] == '.pdf':
            attach_file_name = pdf_body
            attach_file = open(attach_file_name, 'rb')
            pass

        print(id_pass,send_to,subject,text_body,pdf_body)
        print(sender_address, sender_pass)

        message = MIMEMultipart()
        message['From'] = sender_address
        message['Subject'] = subject
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(sender_address, sender_pass)
        message.attach(MIMEText(mail_content, 'plain'))
        if attach_file_name[-4:]=='.pdf':
            payload = MIMEBase('application', 'octate-stream')
            payload.set_payload((attach_file).read())
            encoders.encode_base64(payload)  # encode the attachment
            # add payload header with filename
            payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
            message.attach(payload)

        for i in range(len(data)):
            receiver_address = data.iloc[i, 0]
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            print('Mail Sent to: ',receiver_address)

        stage_label['bg'] = 'light green'
        stage_label['text'] = 'Done'






    except TypeError:
        update_label['bg'] = 'Red'
        update_label['text'] = 'Please provide file correctly'
        print('Please provide file correctly........')

    except IndexError:
        print('Please provide file correctly')

    finally:
        n.close()
         #File Closing section


def reset_all():
    button_explore1['state'] = 'normal'
    button_explore2['state'] = 'normal'
    button_explore3['state'] = 'normal'
    button_explore4['state'] = 'normal'
    button_explore5['state'] = 'normal'
    stage_label['bg'] = '#dff2f2' #text='Entry stage',bg='#dff2f2'
    stage_label['text'] = 'Entry stage'
    E1_file.set('')
    E2_file.set('')
    E3_file.set('')
    E4_file.set('')
    E5_file.set('')
    update_label['bg'] = '#dff2f2'
    update_label['text'] = 'Update here'


# Create the root window
window = Tk()
E1_file=StringVar()
E2_file=StringVar()
E3_file=StringVar()
E4_file=StringVar()
E5_file=StringVar()


# Set window title
window.title('File Explorer')

# Set window size
window.geometry("500x500")

# Set window background color
window.config(background="#dff2f2")

# Create a File Explorer label
label_file_explorer = Label(window,text="Email Sender",fg="black",font=('calibre',13, 'bold'))
label_file_explorer.place(x=1, y=1,height=20, width=500)

################################## ID password file
button_explore1 = Button(window,text="Sender IDpass",command=browse_idpass_Files)
button_explore1.place(x=400, y=40,height=20, width=80)

E1 = Entry(window,textvariable = E1_file, bd=1)
E1.place(x=10, y=40,height=20, width=350)

################################## Emails send excel file
button_explore2 = Button(window,text="Email send to",command=browse_email_send_to_Files)
button_explore2.place(x=400, y=80,height=20, width=80)

E2 = Entry(window,textvariable = E2_file, bd=1)
E2.place(x=10, y=80,height=20, width=350)

################################## Emails Subject file
button_explore3 = Button(window,text="Subject",command=browse_subject_Files)
button_explore3.place(x=400, y=120,height=20, width=80)

E3 = Entry(window,textvariable = E3_file, bd=1)
E3.place(x=10, y=120,height=20, width=350)

################################## Emails Body file
button_explore4 = Button(window,text="Text Body",command=browse_body_Files)
button_explore4.place(x=400, y=160,height=20, width=80)

E4 = Entry(window,textvariable = E4_file, bd=1)
E4.place(x=10, y=160,height=20, width=350)

################################## Emails pdf file
button_explore5 = Button(window,text="PDF",command=browse_pdf_Files)
button_explore5.place(x=400, y=200,height=20, width=80)

E5 = Entry(window,textvariable = E5_file, bd=1)
E5.place(x=10, y=200,height=20, width=350)

send =  Button(window,text="Send",bg='red',command=send_mail)
send.place(x=275, y=400,height=30, width=150)

# creating a state
stage_label = tk.Label(window, text='Entry stage',bg='#dff2f2', font=('calibre', 10, 'bold'))
stage_label.place(x=100, y=400,height=30, width=100)

update_label = tk.Label(window, text='updated here',bg='#dff2f2', font=('calibre', 10))
update_label.place(x=150, y=350,height=30, width=200)

reset_b =  Button(window,text="R",bg='red',bd=2,command=reset_all)
reset_b.place(x=10, y=2,height=18, width=30)

my_label = tk.Label(window, text='by vaibhav',bg='#dff2f2', font=('Segoe Script', 6))
my_label.place(x=450, y=490,height=10, width=50)


button_exit = Button(window,text="Exit",command=exit)
button_exit.place(x=220, y=450,height=20, width=60)

# Let the window wait for any events
window.mainloop()