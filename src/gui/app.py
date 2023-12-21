import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
import customtkinter as ctk

import os

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_widget_scaling(1)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Converter")
        self.geometry(f"{550}x{340}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)


        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(3, weight=1)



        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame,text="Files", command=self.get_start_directory)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame,text="Destination", command=self.get_destination_directory)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame,text="Start", command=self.start)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["System","Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["75%", "100%", "125%", "150%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create middlebar frame with widgets
        self.middlebar_frame = ctk.CTkFrame(self, width=280, corner_radius=0)
        self.middlebar_frame.grid(row=0, column=1,columnspan=3, rowspan=4, sticky="nsew")
        self.middlebar_frame.grid_rowconfigure(3, weight=1)


        self.middlebar_entry_1 = ctk.CTkEntry(self.middlebar_frame)
        self.middlebar_entry_1.grid(row=0, column=1,columnspan=2, padx=20, pady=10)
        self.middlebar_entry_2 = ctk.CTkEntry(self.middlebar_frame)
        self.middlebar_entry_2.grid(row=1, column=1,columnspan=2, padx=20, pady=10)
        
        # create progressbar 
        self.progressbar_1 = ctk.CTkProgressBar(self)
        self.progressbar_1.grid(row=2, column=1, padx=(20, 10), pady=(10, 10), sticky="ew")
        

        self.sidebar_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("System")
        self.scaling_optionemenu.set("100%")
        self.progressbar_1.set(0)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def get_start_directory(self):
        path = self.get_folder_path()
        self.start_path = path
        self.middlebar_entry_1.delete(0, tk.END)
        self.middlebar_entry_1.insert(0,self.start_path)
        self.middlebar_entry_1.update()
        self.check_correctness()


    def get_destination_directory(self):
        path = self.get_folder_path()
        self.dest_path = path
        self.middlebar_entry_2.delete(0, tk.END)
        self.middlebar_entry_2.insert(0,self.dest_path)
        self.middlebar_entry_2.update()
        self.check_correctness()

    def get_folder_path(self):
        path = filedialog.askdirectory()
        return path
    
    def check_correctness(self):
        self.start_path = self.middlebar_entry_1.get()
        self.dest_path = self.middlebar_entry_2.get()
        
        if self.start_path == "":
            return

        if self.dest_path == "":
            return
        
        if not os.path.isdir(self.start_path):
            return
        
        self.sidebar_button_3.configure(state="enabled",text="Start")
    
    def start(self):
        pass
        