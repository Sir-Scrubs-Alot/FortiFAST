import customtkinter
import os
import paramiko
import cmd
import time
import sys
import datetime
import re
import random
from CTkMessagebox import CTkMessagebox
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Forti-Freaking-Awesome-Scripting-Tool")
        self.geometry("700x760")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  FortiFAST", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="New Fortigate Setup",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 2",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        numberAtRandom = (random.randint(1,3))
        if numberAtRandom == 1:
            funQuote = '"Mawage is wot bwings us together today"'

        if numberAtRandom == 2:
            funQuote = '"Its a One-Off"'
            
        if numberAtRandom == 3:
            funQuote = '"Not-Your-Fathers-Executable"'

        my_font = customtkinter.CTkFont(family="Roboto", size=12, slant="italic")

        FunQuote = customtkinter.CTkLabel(self.home_frame,text=funQuote,font=my_font)
        FunQuote.pack(pady=5, padx=5)

        fortigatehostname_label = customtkinter.CTkLabel(self.home_frame,text="Set Hostname:",font=("Roboto", 16))
        fortigatehostname_label.place(x=10, y=100)

        fortigatehostname_entry = customtkinter.CTkEntry(self.home_frame, placeholder_text="EX: ECMSI_FGT60F")
        fortigatehostname_entry.place(x=160, y=100)

        fortipassword_label = customtkinter.CTkLabel(self.home_frame,text="Set Password:",font=("Roboto", 16))
        fortipassword_label.place(x=10, y=150)

        fortipassword_entry = customtkinter.CTkEntry(self.home_frame, placeholder_text="")
        fortipassword_entry.place(x=160, y=150)



        wan1publicip_label = customtkinter.CTkLabel(self.home_frame,text="WAN1 Public IP:",font=("Roboto", 16))
        wan1publicip_label.place(x=10, y=200)

        wan1publicip_entry = customtkinter.CTkEntry(self.home_frame, placeholder_text="")
        wan1publicip_entry.place(x=160, y=200)



        wan1subnet_label = customtkinter.CTkLabel(self.home_frame,text="WAN1 Subnet Mask:",font=("Roboto", 16))
        wan1subnet_label.place(x=10, y=250)

        wan1subnet_entry = customtkinter.CTkEntry(self.home_frame, placeholder_text="EX: 255.255.255.255")
        wan1subnet_entry.place(x=160, y=250)



        ispgateway_label = customtkinter.CTkLabel(self.home_frame,text="ISP Gateway IP:",font=("Roboto", 16))
        ispgateway_label.place(x=10, y=300)

        ispgateway_entry = customtkinter.CTkEntry(self.home_frame, placeholder_text="")
        ispgateway_entry.place(x=160, y=300)



        ipofauvikcollector_label = customtkinter.CTkLabel(self.home_frame,text="Auvik Collector IP:",font=("Roboto", 16))
        ipofauvikcollector_label.place(x=10, y=350)

        ipofauvikcollector_entry = customtkinter.CTkEntry(self.home_frame, placeholder_text="")
        ipofauvikcollector_entry.place(x=160, y=350)




        rocommunitystring_label = customtkinter.CTkLabel(self.home_frame,text="SNMP Community:",font=("Roboto", 16))
        rocommunitystring_label.place(x=10, y=400)

        rocommunitystring_entry = customtkinter.CTkEntry(self.home_frame, placeholder_text="")
        rocommunitystring_entry.place(x=160, y=400)



        phonesystem_checkbox = customtkinter.CTkCheckBox(self.home_frame, text="Allworx Phone System Setup",font=("Roboto", 16))
        phonesystem_checkbox.place(x=10, y=500)



        allworxpublicvip_label = customtkinter.CTkLabel(self.home_frame,text="Allworx Public IP:",font=("Roboto", 16))
        allworxpublicvip_label.place(x=10, y=550)

        allworxpublicvip_entry = customtkinter.CTkEntry(self.home_frame, placeholder_text="")
        allworxpublicvip_entry.place(x=160, y=550)



        allworxprivateip_label = customtkinter.CTkLabel(self.home_frame,text="Allworx Private IP:",font=("Roboto", 16))
        allworxprivateip_label.place(x=10, y=600)

        allworxprivateip_entry = customtkinter.CTkEntry(self.home_frame, placeholder_text="")
        allworxprivateip_entry.place(x=160, y=600)


        def button_hover(e):
            status_Label.configure(text="HOVERING!")

        def button_hover_leave(e):
            status_Label.configure(text="")


        status_Label = customtkinter.CTkLabel(self.home_frame, text='')
        status_Label.pack(side=customtkinter.BOTTOM, fill=customtkinter.X, padx=10,  pady=10)

    
        button = customtkinter.CTkButton(self.home_frame, text="Launch", font=("Roboto", 16))
        button.pack(side=customtkinter.BOTTOM, padx=10,  pady=10)

        button.bind("<Enter>", button_hover)
        button.bind("<Leave>", button_hover_leave)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
