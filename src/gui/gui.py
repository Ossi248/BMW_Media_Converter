import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

import os

import sys

class GUI(tk.Tk):
    def __init__(self, title, size):

        # main setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])

        # widgets
        self.menu = Menu(self)
        self.menubar = Menubar(self)
        self.config(menu=self.menubar)

        #run
        self.mainloop()

class Menubar(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)
        
        # filemenu
        self.fileMenu = tk.Menu(self, tearoff= False)

        # add Menu to Menubar
        self.add_cascade(label='File', underline = 0, menu = self.fileMenu)

        # returns path to Starting Folder 
        self.fileMenu.add_command(label = 'Open start folder')

        # returns path to destination folder
        self.fileMenu.add_command(label = 'Set destination folder')

        self.fileMenu.add_separator()

        # exit program
        self.fileMenu.add_command(label = 'Exit', underline = 1, command = self.quit)


        # helpmenu
        self.helpMenu = tk.Menu(self, tearoff = False)
        
        # add Menu to Menubar
        self.add_cascade(label='Help', underline = 0, menu = self.helpMenu)

        # Shows Info
        self.helpMenu.add_command(label = 'Info', underline = 1)


    def quit(self):
        sys.exit(0)

    def start(self):
        pass


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.start_dir_path = ''
        self.dest_dir_path = ''

        self.place(x=0,y=0, relheight=1, relwidth=1)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):

        # widgets for start folder
        self.start_lable = ttk.Label(self, text = 'Folder with mp3-files')
        self.start_entry =ttk.Entry(self, text= self.start_dir_path)
        self.start_folder_button = ttk.Button(self, text = 'Open', command=self.start_dir)

        # widgets for destination folder
        self.dest_lable = ttk.Label(self, text = 'destination Folder')
        self.dest_entry =ttk.Entry(self, text= self.dest_dir_path + 'Hi')
        self.dest_folder_button = ttk.Button(self, text = 'Open', command=self.dest_dir)

        # start button
        self.start_button = ttk.Button(self, text= 'Start',command=self.start)

        # cancel button
        self.cancel_button = ttk.Button(self, text= 'Cancel',command=self.quit)

        # exit button
        self.exit_button = ttk.Button(self, text= 'Exit',command=self.quit)

        # message label
        self.message_label = ttk.Label(self,text= 'Massages: ')
        self.info_label = ttk.Label(self, text= '')

        self.progressBar = ttk.Progressbar(self, orient='horizontal', mode='determinate', length=280)

    def create_layout(self):

        # create the grid
        self.columnconfigure((0,1,2,), weight=1, uniform='a')
        self.rowconfigure((0,1,2,3,4), weight=1, uniform='a')

        # place the widgets
        self.progressBar.grid(row = 0, column=0,columnspan=3,sticky='nsew')

        self.message_label.grid(row=1,column=0,sticky='nsew')
        self.info_label.grid(row=1, column=1, columnspan=2,sticky='nsew')

        self.start_lable.grid(row = 2, column=0,sticky='nsew')
        self.start_entry.grid(row = 2, column=1,sticky='nsew')
        self.start_folder_button.grid(row = 2, column=2,sticky='nsew')

        self.dest_lable.grid(row = 3, column=0,sticky='nsew')
        self.dest_entry.grid(row = 3, column=1,sticky='nsew')
        self.dest_folder_button.grid(row = 3, column=2,sticky='nsew')

        self.start_button.grid(row = 4, column= 2,sticky='nsew')
        self.cancel_button.grid(row = 4, column= 1,sticky='nsew')
        self.exit_button.grid(row = 4, column= 0,sticky='nsew')

    def fileDialog(self):

        file = fd.askdirectory()
        return file

    def start_dir(self):

        self.start_dir_path = self.fileDialog()
        self.start_entry.delete(0,tk.END)
        self.start_entry.insert(0, self.start_dir_path)
        self.pack()
        
    def dest_dir(self):

        self.dest_dir_path = self.fileDialog()
        self.dest_entry.delete(0,tk.END)
        self.dest_entry.insert(0, self.dest_dir_path)
        self.pack()

    def quit(self):
        sys.exit(0)

    def start(self):
        self.progressBar['value'] = 50


        start_dir = self.start_entry.get()

        s = os.path.isdir(start_dir)
        print(s)

        dest_dir = self.dest_entry.get()
        d = os.path.isdir(dest_dir)
        print(d)
        
        pass