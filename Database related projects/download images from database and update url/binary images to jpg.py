from tkinter import *
import tkinter as tk
from tkinter import ttk
import threading
import pyodbc
import os
import datetime
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time

img_dir = r"C:\Users\ORNET71\Voter_Images"
IMAGE_SIZE = (100, 100)
IMAGES_PER_LOAD = 200


class Dashboard:
    def __init__(self, root):
        self.root = root

        # Set window title
        self.root.title('Image Save From DB and Update DB')

        # Set the window attributes for full screen display above the taskbar
        # root.attributes("-fullscreen", True)
        # Get the dimensions of the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Subtract 30 pixels from the screen dimensions
        window_width = screen_width - 40
        window_height = screen_height - 80

        # Set the window size and position
        self.root.geometry(f"{window_width}x{window_height}+15+15")

        self.root.config(background="#dff2f2")

        self.sidebar = Frame(self.root, bg='#ffffff')
        self.sidebar.place(x=0, y=0, width=235, height=700)
        # Name of brand/person
        self.brandName = Label(self.sidebar, text='ORNET Tech.', bg='#ffffff', font=("", 15, "bold"))
        self.brandName.place(x=50, y=50)

        # basic frame
        self.frame1 = Frame(self.root, bg='light blue')
        # self.frame1.place(x=220, y=1, width=750, height=800)

        self.frame2 = Frame(self.root, bg='white')
        # self.frame2.place(x=220, y=1, width=750, height=800)

        self.frame3 = Frame(self.root, bg='#dff2f2')
        # self.frame3.place(x=220, y=1, width=750, height=800)

        for frame in (self.frame1, self.frame2, self.frame3):
            frame.place(x=240, y=0, width=1100, height=700)

        # Create a list of options for the dropdown menu
        options = self.listDB()  # ['Option 1', 'Option 2', 'Option 3']

        # Create a StringVar object to hold the selected option
        self.selected_option = tk.StringVar()

        # Set the default value of the selected_option to the first option
        self.selected_option.set(options[0])

        # Create the OptionMenu widget
        dropdown = tk.OptionMenu(root, self.selected_option, *options)
        button = tk.Button(root, text='Show', command=self.show_option, padx=10)
        dropdown.place(x=20, y=80, width=120, height=40)
        button.place(x=150, y=80, width=60, height=40)

        root.mainloop()
    def show_option(self):


        # Dashboard
        self.dashboard_text = Button(self.sidebar, text='Analyasis DB', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                     cursor='hand2', activebackground='#ffffff',
                                     command=self.dashboard)
        self.dashboard_text.place(x=50, y=190)

        # Images to URL

        self.manage_text = Button(self.sidebar, text='Work With Images', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff',
                                  command=self.operation)
        self.manage_text.place(x=50, y=220)

        # images view
        self.image_viwer = Button(self.sidebar, text='Saved Images', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff',
                                command=self.image_view)
        self.image_viwer.place(x=50, y=250)

    def dashboard(self):
        self.show_frame(self.frame1)
        self.grid_frame_left_card_1 = tk.Frame(self.frame1, bg='#dff2f2')
        self.label_card_1 = tk.Label(self.grid_frame_left_card_1, text="Total Images in DB", font=("Arial", 12), bg='#dff2f2')
        self.label_count_card_1 = tk.Label(self.grid_frame_left_card_1, text="", font=("Arial", 25), bg='#dff2f2')

        self.grid_frame_left_card_2 = tk.Frame(self.frame1, bg='#dff2f2')
        self.label_card_2 = tk.Label(self.grid_frame_left_card_2, text="Updated Images in DB", font=("Arial", 12), bg='#dff2f2')
        self.label_count_card_2 = tk.Label(self.grid_frame_left_card_2, text="", font=("Arial", 25), bg='#dff2f2')
        # grid_frame_left_card_2.place(x=20, y=330, width=195, height=150)

        self.grid_frame_left_card_3 = tk.Frame(self.frame1, bg='#dff2f2')
        self.label_card_3 = tk.Label(self.grid_frame_left_card_3, text="Pending Images in DB", font=("Arial", 12), bg='#dff2f2')
        self.label_count_card_3 = tk.Label(self.grid_frame_left_card_3, text="", font=("Arial", 25), bg='#dff2f2')

        DB_photo_count, DB_url_count, DB_results_query_not_photo_url_count = self.display_data_fetch()

        display_value = self.display_card(DB_photo_count, DB_url_count, DB_results_query_not_photo_url_count)


    def display_data_fetch(self):
        print(self.selected_option.get())

        # Set up connection parameters
        self.server = 'ORNET71'
        self.database = self.selected_option.get()
        self.driver = '{SQL Server Native Client 11.0}'

        # Set up connection string
        conn_str = f"DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes;"

        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        print(f"connected {self.database}")
        '''conn = pyodbc.connect('Driver= {SQL Server Native Client 11.0};'
                              'Server=ORNET71;'
                              'Database=AC_150;'
                              'Trusted_Connection=yes;')'''
        # execute a SQL query to check if a column is available in a table
        query = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'EROLL' AND COLUMN_NAME = 'PHOTO_URL'"
        cursor.execute(query)

        # check if the query returned any results
        if cursor.fetchone():
            print("Column exists in table")

        else:
            print("Column does not exist in table")

            # execute a SQL query to add a new column to a table
            query = "ALTER TABLE EROLL ADD PHOTO_URL nvarchar(250)"
            cursor.execute(query)

            # commit the changes to the database
            conn.commit()

        # execute a SQL query to check if a column is available in a table
        query_photo_count = "SELECT COUNT(*) FROM dbo.EROLL WHERE PHOTO IS NOT NULL"
        cursor.execute(query_photo_count)

        # fetch the results of the query
        results_count = cursor.fetchall()
        for row in results_count:
            print("total images available in database", row[0])
            DB_photo_count = row[0]

        query_photo_url_count_pending = "SELECT COUNT(*) FROM dbo.EROLL WHERE PHOTO IS NOT NULL AND PHOTO_URL IS NULL"
        cursor.execute(query_photo_url_count_pending)

        # fetch the results of the query
        results_query_photo_url_count = cursor.fetchall()
        for row in results_query_photo_url_count:
            print("Image data for work", row[0])
            DB_results_query_not_photo_url_count = row[0]

        DB_url_count = (DB_photo_count - DB_results_query_not_photo_url_count)

        print("converted", DB_url_count)

        return DB_photo_count, DB_url_count, DB_results_query_not_photo_url_count


    def display_card(self,DB_photo_count, DB_url_count, DB_results_query_not_photo_url_count):
        # frame for PIE chart
        self.grid_frame_graph = tk.Frame(self.frame1, bg='light blue')


        # loading count
        self.label_count_card_1.config(text=DB_photo_count)
        self.label_count_card_2.config(text=DB_url_count)
        self.label_count_card_3.config(text=DB_results_query_not_photo_url_count)

        self.grid_frame_left_card_1.place(x=20, y=70, width=195, height=150)
        self.label_card_1.place(x=2, y=10, width=190, height=20)
        self.label_count_card_1.place(x=18, y=35, width=170, height=40)

        self.grid_frame_left_card_2.place(x=20, y=270, width=195, height=150)
        self.label_card_2.place(x=2, y=10, width=190, height=20)
        self.label_count_card_2.place(x=18, y=35, width=170, height=40)

        self.grid_frame_left_card_3.place(x=20, y=460, width=195, height=150)
        self.label_card_3.place(x=2, y=10, width=190, height=20)
        self.label_count_card_3.place(x=18, y=35, width=170, height=40)


        self.grid_frame_graph.place(x=260, y=65, width=545, height=545)
        self.drawPieChart([DB_url_count, DB_results_query_not_photo_url_count], ['Converted', 'Not Converted'], self.grid_frame_graph)

        return True


    def operation(self):
        self.show_frame(self.frame2)

        self.operation_button_frame = tk.Frame(self.frame2, bg='#dff2f2')
        self.start_card= tk.Button(self.operation_button_frame, text="Start", font=("Arial", 12),bg='light green', command=self.threat_download_upoload)
        self.stop_card = tk.Button(self.operation_button_frame, text="Stop", font=("Arial", 12), bg='red')

        self.operation_button_frame.place(x=30, y=0, width=1000, height=700)
        self.start_card.place(x=120, y=80, width=60, height=40)
        self.stop_card.place(x=20, y=80, width=60, height=40)



    def threat_download_upoload(self):

        # create a new thread to update the database
        self.thread = threading.Thread(target=self.download_upload_url())
        self.thread.start()
        self.thread.stop()

    def download_upload_url(self):
        print('starting')
        # Set up connection parameters
        self.server = 'ORNET71'
        self.database = self.selected_option.get()
        self.driver = '{SQL Server Native Client 11.0}'

        # Set up connection string
        conn_str = f"DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes;"

        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()
        round=0

        # create a progress bar
        self.progress = ttk.Progressbar(self.frame2, orient="horizontal", length=500, mode="determinate")
        self.progress.place(x=200, y=300)

        self.updated_count = Label(self.frame2, text='', bg='#ffffff', font=("", 15, "bold"))
        self.updated_count.place(x=150, y=250)

        while round < 100:
            query = "SELECT TOP (500) AUTO_ID, AC_NO, EPIC_NO, PHOTO FROM dbo.EROLL WHERE PHOTO IS NOT NULL AND PHOTO_URL IS NULL"
            self.cursor.execute(query)

            # fetch the results of the query
            results = self.cursor.fetchall()
            i = 1

            for row in results:
                # print(row)
                image_data = row[3]

                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")

                saved_path = os.path.join(r"C:\Users\ORNET71\Voter_Images",
                                          "{}_{}_{}_{}.jpg".format(timestamp, row[0], row[1], row[2])).replace(" ", "")

                print(saved_path)

                with open(os.path.join(saved_path), "wb") as f:
                    f.write(image_data)

                query_update = "UPDATE dbo.EROLL SET PHOTO_URL = '{}' WHERE AUTO_ID = '{}' AND EPIC_NO = '{}'".format(
                    saved_path, row[0], row[2])
                print(query_update)
                self.cursor.execute(query_update)

                # Commit the changes to the database
                self.conn.commit()

                print(f"saved {i} out off 500 and updated on local database for round {round}")

                self.updated_count.config(text=f"saved {i}/500 and updated on local database for round {round}/100")
                # update the progress bar
                self.progress["value"] = (i / 100)
                self.frame2.update()

                # pause for half a second
                time.sleep(0.5)
                i += 1

            #self.graph = tk.Frame(self.frame2, bg='white')
            round += 1
            #self.graph.place(x=260, y=65, width=545, height=545)
            #self.drawPieChart([round, 6-round], ['Converted', 'Not Converted'],self.graph)

            # Close the cursor and the connection
        self.cursor.close()
        self.conn.close()

    def stop_operation(self):
        self.thread.stop()
        self.cursor.close()
        self.conn.close()

    def image_view(self):
        self.show_frame(self.frame3)

        scrollbar = ttk.Scrollbar(self.frame3)
        scrollbar.pack(side='right', fill='y')

        # Create a canvas for the images
        self.canvas = tk.Canvas(self.frame3, yscrollcommand=scrollbar.set)
        self.canvas.pack(side='left', fill='both', expand=True)

        # Configure the scrollbar to scroll the canvas
        scrollbar.config(command=self.canvas.yview)

        # Create a frame to hold the images
        self.image_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.image_frame, anchor='nw')

        # Load the images
        self.img_list = os.listdir(img_dir)[:200]  # Load the first 200 images
        for i, img_file in enumerate(self.img_list):
            img_path = os.path.join(img_dir, img_file)
            img = Image.open(img_path)
            img = img.resize((150, 150))  # Resize the image
            photo = ImageTk.PhotoImage(img)
            label = tk.Label(self.image_frame, image=photo)
            label.photo = photo
            label.grid(row=i // 10, column=i % 10, padx=5, pady=5)  # Display the image

        # Configure the canvas to resize with the window
        self.image_frame.bind('<Configure>', lambda event: self.canvas.configure(scrollregion=self.canvas.bbox('all')))

        # Create a button to load more images
        more_button = tk.Button(self.frame3, text='Load more images', command=self.load_more_images)
        more_button.place(x=10, y=630)

    # Function to load more images
    def load_more_images(self):
        start_index = len(self.img_list)
        end_index = start_index + 200
        more_images = os.listdir(img_dir)[start_index:end_index]
        for i, img_file in enumerate(more_images):
            img_path = os.path.join(img_dir, img_file)
            img = Image.open(img_path)
            img = img.resize((150, 150))
            photo = ImageTk.PhotoImage(img)
            label = tk.Label(self.image_frame, image=photo)
            label.photo = photo
            label.grid(row=(i + start_index) // 10, column=(i + start_index) % 10, padx=5, pady=5)
        self.img_list.extend(more_images)
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def show_frame(self, frame):
        frame.tkraise()

    # return list of databases
    def listDB(self):
        # Set up the database connection
        conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=ORNET71;"
                              "Trusted_Connection=yes;")

        # Execute a query to retrieve the list of databases
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sys.databases")
        DB_list = []
        for row in cursor:
            DB_list.append(row[0])

        # Close the cursor and the connection
        cursor.close()
        conn.close()

        return DB_list

    def drawPieChart(self, data, labels, master):
        # create a figure and axis object for the pie chart
        fig = Figure(figsize=(5, 5))
        ax = fig.add_subplot(111)

        # create the pie chart
        ax.pie(data, labels=labels)

        # create a canvas to display the pie chart
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.draw()

        # pack the canvas into the window
        canvas.get_tk_widget().place(x=10, y=2, width=480, height=400)

    def stop_count(self):
        self.running = False

    def run(self):
        self.root.mainloop()


def win():
    root = Tk()
    Dashboard(root)  # , data)
    root.mainloop()


if __name__ == '__main__':
    win()