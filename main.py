import tkinter
from tkinter import *
from tkinter import ttk
import time
import random
import csv
from tkinter import messagebox
import customtkinter
import pygame
from pygame import mixer
mixer.init()

compte_dictionary = {-1:1234}
name_dictionary = {-1:"lahcen skaih"}
CNI_dictionary = {-1:"JA187209"}
gmail_dictionary = {-1:"lahcenenligne@gamil.com"}
phone_dictionary = {-1:"0642384925"}
city_dictionary={-1:"Guelmim"}
solde_dictionary = {-1:10000}
numbre_card_dictionary= {-1:"1234-1235-1236-1237"}
list_time = time.gmtime()
date= f"{list_time[1]}/{list_time[2]}/{list_time[0]}"
date_dictionary = {-1:"02/02/2023"}
list_number_carde = []
list_heading_file = ["Number Client","Full Name","Password","CNI","Gmail","Phone","City","Solde","Numbre Card Bank","Date Of Create"]
dictionary_file = {"Number Client":-1,"Full Name":"lahcen skaih","Password":1234,"CNI":"JA187209 ","Gmail":"lahcenenlign@gmail.com","Phone":"0642384925","City":"guelmim".capitalize(),"Solde":f"{10000} ","Numbre Card Bank":"1234-1235-1236-1237","Date Of Create":"02/02/2023"}


class show_interface():

    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.windows = customtkinter.CTk()
        self.windows.title('lsbank'.upper())
        self.windows.iconbitmap("bank.ico")
        self.windows.geometry("1000x800")
        
        self.text =customtkinter.CTkLabel(self.windows,
                     text="welcome in ".capitalize()+"lsbank".upper(),
                     font=('Arial',40,'bold'),
                     
                     )
        self.text.pack()
        
    
    def interface(self):
       
        self.windows.mainloop()


class agent(show_interface):


    
    def check_agent(self):
        self.windows
        self.ask1 = customtkinter.CTkLabel(self.windows,
                         text="Enter your name: ",
                         font=("Arial",20,"bold"))
        self.ask1 .place(x=20,y=100)

        self.ask_text1 = customtkinter.CTkEntry(self.windows,
                              width=180,height=30)
        self.ask_text1.place(x=290,y=100)

        self.ask2 =customtkinter.CTkLabel(self.windows,
                         text="Enter the secret code: ",
                         font=("Arial",20,"bold"))
        
        self.ask2 .place(x=20,y=150)
        self.ask_text2 = customtkinter.CTkEntry(self.windows,
                              width=180,height=30)
        self.ask_text2.place(x=290,y=150)

        # self.btn1img = PhotoImage(file="submit.png")
        self.btn1 = customtkinter.CTkButton(self.windows,
                           text="Submit",
                           border_width=1,
                           command=self.submit_check,
                           width=100,
                           ) 
        self.btn1.place(x=250,y=200)
        

        
    def destro(self):
        self.title.destroy()
        self.deletebtn.destroy()

    def add_client(self):
        try:
            self.suprimerbtn.destroy()
            self.addbtn.destroy()
            self.data_base_btn.destroy()
            self.destro()
            
            self.opening = pygame.mixer.Sound(file="opening.wav")
            self.opening.play()
            
            

            self.form_1 = customtkinter.CTkFrame(self.windows,
                                                width=400,
                                                height=500,
                                                corner_radius=16
                                                )
            self.form_1.place(relx=0.5,rely=0.6,anchor=tkinter.CENTER)
            self.login_text = customtkinter.CTkLabel(self.form_1,
                                                    text="Add user",
                                                    font=("Arial",20,"bold"),
                                                    
                                                    )
            self.login_text.place(x=150,y=20)
            self.text_number_user = customtkinter.CTkLabel(self.form_1,
                                                        text="Enter the number of user:",
                                                        font=("Arial",15,"bold"),
                                                        text_color="white")
            self.text_number_user.place(x=20,y=60)
            self.Entry_user = customtkinter.CTkEntry(self.form_1,
                                                    width=140,
                                                    height=30,
                                                    border_width=1,
                                                    placeholder_text="number of the client"
                                                    )
            # make numbre generate autoumatic
            with open("data_client.csv","r") as f:
                f.__next__()
                for self.line in f:
                    self.str_key_file = self.line[0]
            self.int_key_file = int(self.str_key_file)
                
            
            self.Entry_user.insert(0,self.int_key_file+1)
            self.Entry_user.place(y=60,x=240)

            self.name_user = customtkinter.CTkLabel(self.form_1,
                                                    text="Enter the full name:",
                                                    font=("Arial",15,"bold"),
                                                    )
            self.name_user.place(x=20,y=120)
            self.Entry_name_user = customtkinter.CTkEntry(self.form_1,
                                                    width=140,
                                                    height=30,
                                                    border_width=1,
                                                    placeholder_text="full name"
                                                    )
            self.Entry_name_user.place(x=240,y=120)
            self.CNI = customtkinter.CTkLabel(self.form_1,
                                            text="enter CNI :",
                                            font=("Arial",15,"bold"))
            self.CNI.place(x=20,y=180)
            self.Entry_CNI = customtkinter.CTkEntry(self.form_1,
                                                    width=140,
                                                    height=30,
                                                    placeholder_text="numbre card national",
                                                    border_width=1
                                                    )
            self.Entry_CNI.place(x=240,y=180)
            self.phone = customtkinter.CTkLabel(self.form_1,
                                                text="Enter phone numbre:",
                                                font=("Arial",15,"bold"))
            self.phone.place(x=20,y=240)
            self.Entry_phone = customtkinter.CTkEntry(self.form_1,
                                                    width=140,
                                                    height=30,
                                                    border_width=1,
                                                    placeholder_text="+212600000001")
            self.Entry_phone.place(y=240,x=240)
            self.gamil = customtkinter.CTkLabel(self.form_1,
                                                text="enter gmail:",
                                                font=("Arial",15,"bold"))
            self.gamil.place(x=20,y=300)
            self.Entry_gmail = customtkinter.CTkEntry(self.form_1,
                                                    width=140,
                                                    height=30,
                                                    placeholder_text="@gmail.com",
                                                    border_width=1,)
            self.Entry_gmail.place(x=240,y=300)
            self.date = customtkinter.CTkLabel(self.form_1,
                                            text="Date of create account:",
                                            font=("Arial",15,"bold"))
            self.date.place(x=20,y=360)
            self.Entry_date = customtkinter.CTkEntry(self.form_1,
                                                    width=140,
                                                    height=30,
                                                    border_width=1)
            self.Entry_date.insert(0,date)
            self.Entry_date.place(x=240,y=360)


            self.btn_create = customtkinter.CTkButton(self.form_1,
                                                    width=140,
                                                    height=28,
                                                    text="create",
                                                    font=("Arial",15,"bold"),
                                                    
                                                    fg_color="green",
                                                    hover_color="#046b04",
                                                    command=self.info_new_client)
            self.btn_create.place(x=120,y=420)
            self.form_3.destroy()
            self.scrolX.destroy()
            self.scrolY.destroy()
        except AttributeError:
            print("there is a problem but dont worry we are working at it to fix it")

    
    def info_new_client(self):
        pw1 = random.randint(1,9)
        pw2 = random.randint(0,9)
        pw3 = random.randint(0,9)
        pw4 = random.randint(0,9)
        self.pwd = int(str(pw1)+str(pw2)+str(pw3)+str(pw4))
        compte_dictionary.update({self.int_key_file+1:self.pwd})
        date_dictionary.update({self.int_key_file+1:self.Entry_date.get()})
        name_dictionary.update({self.int_key_file+1:self.Entry_name_user.get()})
        CNI_dictionary.update({self.int_key_file+1:self.Entry_CNI.get()})
        gmail_dictionary. update({self.int_key_file+1:self.Entry_gmail.get()})
        phone_dictionary.update({self.int_key_file+1:self.Entry_phone.get()})
        for self.l in range(1,5):
            pww1 = random.randint(1,9)
            pww2 = random.randint(1,9)
            pww3 = random.randint(1,9)
            pww4 = random.randint(1,9)
            pwd1 = int(str(pww3)+str(pww2)+str(pww1)+str(pww4))
            list_number_carde.append(str(pwd1))
        self.number_card = "-".join(list_number_carde)
        self.form_1.destroy()
        self.form_2 = customtkinter.CTkFrame(self.windows,
                                             width=800,
                                             height=600,
                                             corner_radius=20)
        self.form_2.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
        self.name_user1 = customtkinter.CTkLabel(self.form_2,
                                                text="Full name:",
                                                font=("Arial",15,"bold")
                                                )
        self.name_user1.place(x=20,y=60)
        self.Entry_name_user1 = customtkinter.CTkEntry(self.form_2,
                                                      width=140,
                                                      height=30,
                                                      placeholder_text="lahcen skaih"
                                                      )
        self.Entry_name_user1.insert(0,name_dictionary[self.int_key_file+1])
        self.Entry_name_user1.place(y=60,x=200)
        self.text_number1 = customtkinter.CTkLabel(self.form_2,
                                                   text="number of client:",
                                                   font=("Arial",15,"bold"))
        self.text_number1.place(x=20,y=120)
        self.Entry_number1 = customtkinter.CTkEntry(self.form_2,
                                                   width=140,
                                                   height=30,
                                                   placeholder_text="Eemple:1 or 2..."
                                                   )
        self.Entry_number1.insert(0,self.int_key_file+1)
        self.Entry_number1.place(y=120,x=200)
        self.CNi1 = customtkinter.CTkLabel(self.form_2,
                                           text="CNI :",
                                           font=("Arial",15,"bold"))
        self.CNi1.place(x=20,y=180)
        self.Entry_CNI1 = customtkinter.CTkEntry(self.form_2,
                                                 width=140,
                                                 height=30,
                                                 placeholder_text="JA187209")
        self.Entry_CNI1.insert(0,CNI_dictionary[self.int_key_file+1])
        self.Entry_CNI1.place(y=180,x=200)
        self.phone1 = customtkinter.CTkLabel(self.form_2,
                                             text="phone numbre:",
                                             font=("Arial",15,"bold"))
        self.phone1.place(x=20,y=240)
        self.Entry_phone1 = customtkinter.CTkEntry(self.form_2,
                                             width=140,
                                             height=30,
                                             placeholder_text="+212600000001")
        self.Entry_phone1.insert(0,phone_dictionary[self.int_key_file+1])
        self.Entry_phone1.place(y=240,x=200)
        self.solde = customtkinter.CTkLabel(self.form_2,
                                            text="solde of client: ",
                                            font=("Arial",15,"bold"))
        self.solde.place(x=20,y=300)
        self.Entry_solde = customtkinter.CTkEntry(self.form_2,
                                                  width=140,
                                                  height=30,
                                                  placeholder_text="100 ")
        self.Entry_solde.place(y=300,x=200)
        self.password1 = customtkinter.CTkLabel(self.form_2,
                                               text="the password of this client:",
                                               font=("Arial",15,"bold"))
        self.password1.place(x=400,y=60)
        self.Entry_password1 = customtkinter.CTkEntry(self.form_2,
                                                     width=140,
                                                     height=30,
                                                     placeholder_text="4582"
                                                     )
        self.Entry_password1.insert(0,compte_dictionary[self.int_key_file+1])
        self.Entry_password1.place(y=60,x=620)
        self.gmail1 = customtkinter.CTkLabel(self.form_2,
                                            text="the gmail of client",
                                            font=("Arial",15,"bold"))
        self.gmail1.place(x=400,y=120)
        self.Entry_gmail1 = customtkinter.CTkEntry(self.form_2,
                                                   width=140,
                                                   height=30,
                                                   placeholder_text="lahcenenligne@gmail.com")
        self.Entry_gmail1.insert(0,gmail_dictionary[self.int_key_file+1])
        self.Entry_gmail1.place(x=620,y=120)
        self.date1 = customtkinter.CTkLabel(self.form_2,
                                            text="date of create:",
                                            font=("Arial",15,"bold"))
        self.date1.place(x=400,y=180)
        self.Entry_date1 = customtkinter.CTkEntry(self.form_2,
                                                  width=140,
                                                  height=30,
                                                  placeholder_text="2/15/2023")
        self.Entry_date1.insert(0,date_dictionary[self.int_key_file+1])
        self.Entry_date1.place(y=180,x=620)
        self.number_card1 = customtkinter.CTkLabel(self.form_2,
                                                   text="the number card:",
                                                   font=("Arial",15,"bold"))
        self.number_card1.place(x=400,y=240)
        self.Entry_number_card = customtkinter.CTkEntry(self.form_2,
                                                        width=140,
                                                        height=30,
                                                        placeholder_text="XXXX-XXXX-XXXX-XXXX",
                                                        )
        self.Entry_number_card.insert(0,self.number_card)
        self.Entry_number_card.place(y=240,x=620)
        # list_number_carde.clear()
        
        self.city = customtkinter.CTkLabel(self.form_2,
                                           text="Enter your city:",
                                           font=("Arial",15,"bold"))
        self.city.place(x=400,y=300)
        self.Entry_city = customtkinter.CTkEntry(self.form_2,
                                                 width=140,
                                                 height=30,
                                                 placeholder_text="Guelmim")
        self.Entry_city.place(y=300,x=620)
        self.btn_create = customtkinter.CTkButton(self.form_2,
                                                  width=140,
                                                  height=28,
                                                  text="Save",
                                                  font=("Arial",15,"bold"),
                                                  fg_color="green",
                                                  hover_color="#046b04",
                                                  command=self.Save_client)
        self.btn_create.place(x=320,y=420)
    def Save_client(self):
        try:
            self.color= "red"
            if len(self.Entry_city.get()) == 0:
                self.Entry_city = customtkinter.CTkEntry(self.form_2,
                                                    width=140,
                                                    height=30,
                                                    placeholder_text="Guelmim",
                                                    border_color=self.color)
                self.Entry_city.place(y=300,x=620)
            if len(self.Entry_name_user1.get()) == 0:
                self.Entry_name_user1 = customtkinter.CTkEntry(self.form_2,
                                                        width=140,
                                                        height=30,
                                                        placeholder_text="lahcen skaih",
                                                        border_color=self.color
                                                        )
                
                self.Entry_name_user1.place(y=60,x=200)
            if len(self.Entry_number1.get()) == 0:
                self.Entry_number1 = customtkinter.CTkEntry(self.form_2,
                                                    width=140,
                                                    height=30,
                                                    placeholder_text="Eemple:1 or 2...",
                                                    border_color=self.color
                                                    )
                self.Entry_number1.insert(0,self.int_key_file+1)
                self.Entry_number1.place(y=120,x=200)
            if len(self.Entry_CNI1.get()) == 0 :
                self.Entry_CNI1 = customtkinter.CTkEntry(self.form_2,
                                                    width=140,
                                                    height=30,
                                                    placeholder_text="JA187209",
                                                    border_color=self.color)
                self.Entry_CNI1.place(y=180,x=200)
            if len(self.Entry_phone1.get()) == 0:
                self.Entry_phone1 = customtkinter.CTkEntry(self.form_2,
                                                width=140,
                                                height=30,
                                                placeholder_text="+212600000001",
                                                border_color=self.color)
                self.Entry_phone1.place(y=240,x=200)
            if len(self.Entry_solde.get()) == 0:
                self.Entry_solde = customtkinter.CTkEntry(self.form_2,
                                                    width=140,
                                                    height=30,
                                                    placeholder_text="100 ",\
                                                    border_color=self.color)
                self.Entry_solde.place(y=300,x=200)
            if len(self.Entry_password1.get()) == 0:
                self.Entry_password1 = customtkinter.CTkEntry(self.form_2,
                                                        width=140,
                                                        height=30,
                                                        placeholder_text="4582",
                                                        border_color=self.color
                                                        )
                self.Entry_password1.insert(0,compte_dictionary[self.int_key_file+1])
                self.Entry_password1.place(y=60,x=620)
            if len(self.Entry_gmail1.get()) == 0:
                self.Entry_gmail1 = customtkinter.CTkEntry(self.form_2,
                                                    width=140,
                                                    height=30,
                                                    placeholder_text="lahcenenligne@gmail.com",
                                                    border_color=self.color)
                self.Entry_gmail1.insert(0,gmail_dictionary[self.int_key_file+1])
                self.Entry_gmail1.place(x=620,y=120)
            if len(self.Entry_date1.get()) == 0:
                self.Entry_date1 = customtkinter.CTkEntry(self.form_2,
                                                    width=140,
                                                    height=30,
                                                    placeholder_text="2/15/2023",
                                                    border_color=self.color)
                self.Entry_date1.insert(0,date_dictionary[self.int_key_file+1])
                self.Entry_date1.place(y=180,x=620)
            if len(self.Entry_number_card.get()) == 0 :
                list_number_carde.clear()
                self.Entry_number_card = customtkinter.CTkEntry(self.form_2,
                                                            width=140,
                                                            height=30,
                                                            placeholder_text="XXXX-XXXX-XXXX-XXXX",
                                                            border_color=self.color
                                                            )
                self.Entry_number_card.insert(0,self.number_card)
                self.Entry_number_card.place(y=240,x=620)
            
            if len(self.Entry_number_card.get()) > 0 and len(self.Entry_city.get()) > 0 and len(self.Entry_name_user1.get()) > 0 and len(self.Entry_number1.get()) > 0 and len(self.Entry_CNI1.get()) > 0 and len(self.Entry_phone1.get()) >0 and len(self.Entry_solde.get()) > 0 and len(self.Entry_password1.get()) > 0 and len(self.Entry_gmail1.get()) > 0 and len(self.Entry_date1.get()) > 0 and len(self.Entry_number_card.get()) > 0:

                            print(self.result_file())
                                
                                
                       
        except RuntimeError:
            print("save the client has been succesfull")
    
    def result_file(self):
        with open("data_client.csv", "r") as f:
            f.__next__()
            
            # Check if the value already exists in the file
            for row in f:
                if int(row[0]) == int(self.Entry_number1.get()):
                    self.Entry_number1 = customtkinter.CTkEntry(
                        self.form_2,
                        width=140,
                        height=30,
                        placeholder_text="Number already exists",
                        border_color=self.color
                    )
                    self.Entry_number1.place(y=120, x=200)
                    return "no"
                if int(row[0]) > int(self.Entry_number1.get()):
                    self.Entry_number1 = customtkinter.CTkEntry(
                        self.form_2,
                        width=140,
                        height=30,
                        placeholder_text="Number wrong",
                        border_color=self.color
                    )
                    self.Entry_number1.place(y=120, x=200)
                    return 
            else:
                compte_dictionary.update({int(self.Entry_number1.get()):self.pwd})
                date_dictionary.update({int(self.Entry_number1.get()):self.Entry_date1.get()})
                name_dictionary.update({int(self.Entry_number1.get()):self.Entry_name_user1.get()})
                CNI_dictionary.update({int(self.Entry_number1.get()):self.Entry_CNI1.get()})
                gmail_dictionary. update({int(self.Entry_number1.get()):self.Entry_gmail1.get()})
                phone_dictionary.update({int(self.Entry_number1.get()):self.Entry_phone1.get()})
                city_dictionary.update({int(self.Entry_number1.get()):self.Entry_city.get()})
                solde_dictionary.update({int(self.Entry_number1.get()):self.Entry_solde.get()})
                numbre_card_dictionary.update({int(self.Entry_number1.get()):self.Entry_number_card.get()})
                dictionary_file.update({"Number Client":int(self.Entry_number1.get()),"Full Name":self.Entry_name_user1.get(),"Password":self.pwd,"CNI":self.Entry_CNI1.get(),"Gmail":self.Entry_gmail1.get(),"Phone":self.Entry_phone1.get(),"City":self.Entry_city.get(),"Solde":f"{self.Entry_solde.get()} ","Numbre Card Bank":self.Entry_number_card.get(),"Date Of Create":self.Entry_date1.get()})
            
            # If the value does not exist, append a new row to the file
                
                with open("data_client.csv","a",newline="") as f:
                    client_file = csv.DictWriter(f,fieldnames=list_heading_file,delimiter=",")
                    client_file.writerow(dictionary_file)
                    list_number_carde.clear()
                self.btn_create = customtkinter.CTkButton(self.form_2,
                                                                    width=140,
                                                                    height=28,
                                                                    text="Save",
                                                                    font=("Arial",15,"bold"),
                                                                    fg_color="green",
                                                                    hover_color="#046b04",
                                                                    state=DISABLED)
                self.btn_create.place(x=320,y=420)
                self.go_home = customtkinter.CTkButton(self.form_2,width=140,
                                                    height=28,
                                                    text="go_home",
                                                    font=("Arial",15,"bold"),
                                                    command=self.submit)
                self.go_home.place(x=0,y=0)
                return "New client added to file"


                    
    def submit(self):

        self.form_1.destroy()
        self.form_2.destroy()
        
        self.addbtn =customtkinter.CTkButton(self.windows,
                                text="Add user",
                                font=("Arial",15,"bold"),
                                command=self.add_client,
                                fg_color="green",
                                hover_color="#046b04"
                                )
        
        
        self.suprimerbtn =customtkinter.CTkButton(self.windows,
                                text="Delete user",
                                fg_color="red",
                                font=("Arial",15,"bold"),
                                hover_color="#c20c0c",
                                command=self.suprimer_client,
                                )
        self.suprimerbtn.place(x=400,y=200)
        self.addbtn.place(x=600,y=200)
        self.data_base_btn = customtkinter.CTkButton(self.windows,
                                                      text="show data",
                                                      font=("Arial",15,"bold"),
                                                      command=self.show_data_base)
        self.data_base_btn.place(x=500,y=400)
        
        
    def show_data_base(self):
        self.addbtn.destroy()
        self.deletebtn.destroy()
        self.suprimerbtn.destroy()
        self.data_base_btn.destroy()
        self.destro()
        self.form_3 = customtkinter.CTkFrame(self.windows,
                                             width=800,
                                             height=600,
                                             corner_radius=16,
                                             border_color="black",
                                             border_width=1)
        self.form_3.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
        self.scrolX = Scrollbar(self.windows,orient=HORIZONTAL)
        self.scrolY = Scrollbar(self.windows)
        self.scrolX.pack(side=BOTTOM,fill=X)
        self.scrolY.pack(side=RIGHT,fill=Y)
        text_data = ttk.Treeview(self.form_3,
                            xscrollcommand=self.scrolX,
                            yscrollcommand=self.scrolY)
        text_data.place(relx=0.0259,rely=0.1,width=760,height=400)
        text_data.configure(columns=(
            "Number Client",
            "Full Name",
            "Password",
            "CNI",
            "Gmail",
            "Phone",
            "City",
            "Solde",
            "Numbre Card Bank",
            "Date Of Create"
            )
        )
        self.scrolX.configure(command=text_data.xview)
        self.scrolY.configure(command=text_data.yview)
        text_data.heading("#0",text="Id",anchor=W)
        text_data.heading("#1",text="Number Client",anchor=W)
        text_data.heading("#2",text="Full Name",anchor=W)
        text_data.heading("#3",text="Password",anchor=W)
        text_data.heading("#4",text="CNI",anchor=W)
        text_data.heading("#5",text="Gmail",anchor=W)
        text_data.heading("#6",text="Phone",anchor=W)
        text_data.heading("#7",text="City",anchor=W)
        text_data.heading("#8",text="Solde",anchor=W)
        text_data.heading("#9",text="Numbre Card Bank",anchor=W)
        text_data.heading("#10",text="Date Of Create",anchor=W)

        text_data.column("#0",stretch=NO,minwidth=160,width=160)
        text_data.column("#1",stretch=NO,minwidth=160,width=200)
        text_data.column("#2",stretch=NO,minwidth=160,width=160)
        text_data.column("#3",stretch=NO,minwidth=160,width=160)
        text_data.column("#4",stretch=NO,minwidth=160,width=200)
        text_data.column("#5",stretch=NO,minwidth=160,width=200)
        text_data.column("#6",stretch=NO,minwidth=160,width=120)
        text_data.column("#7",stretch=NO,minwidth=160,width=120)
        text_data.column("#8",stretch=NO,minwidth=200,width=200)
        text_data.column("#9",stretch=NO,minwidth=160,width=200)
        text_data.column("#10",stretch=NO,minwidth=160,width=200)
        with open("data_client.csv","r") as db:
            file_db = csv.DictReader(db)
            count = 0
            id = 0
            for line in file_db:
                count += 1
                dictionary_db = {"Number Client":line["Number Client"],"Full Name":line["Full Name"],"Password":line["Password"],"CNI":line["CNI"],"Gmail":line["Gmail"],"Phone":line["Phone"],"City":line["City"],"Solde":f"{line['Solde']} ","Numbre Card Bank":line["Numbre Card Bank"],"Date Of Create":line["Date Of Create"]}
                text_data.insert(parent="",index="end",text=f"000{count}",iid=id,values=(line["Number Client"],line["Full Name"],line["Password"],line["CNI"],line["Gmail"],line["Phone"],line["City"],line["Solde"],line["Numbre Card Bank"],line["Date Of Create"]))
                id += 1
                dictionary_db.clear()
        self.addbtn =customtkinter.CTkButton(self.form_3,
                                 text="Add user",
                                 font=("Arial",15,"bold"),
                                 command=self.add_client,
                                 fg_color="green",
                                 hover_color="#046b04"
                                 )
            
        self.suprimerbtn =customtkinter.CTkButton(self.form_3,
                                text="Delete user",
                                fg_color="red",
                                font=("Arial",15,"bold"),
                                hover_color="#c20c0c",
                                command=self.suprimer_client,
                                )
        self.suprimerbtn.place(x=400,y=500)
        self.addbtn.place(x=600,y=500)
    



    
    
    def suprimer_client(self):
        
        self.addbtn.destroy()
        self.destro()
        self.suprimerbtn.destroy()
        self.data_base_btn.destroy()
        self.form_1 = customtkinter.CTkFrame(self.windows,
                                             width=400,
                                             height=500,
                                             corner_radius=16
                                             )
        self.form_1.place(relx=0.5,rely=0.6,anchor=tkinter.CENTER)
        self.login_text = customtkinter.CTkLabel(self.form_1,
                                                 text="Delete user",
                                                 font=("Arial",20,"bold"),
                                                 
                                                 )
        self.login_text.place(x=150,y=20)
        self.list_number = []
        self.text_number_user = customtkinter.CTkLabel(self.form_1,
                                                       text="Enter the number of user:",
                                                       font=("Arial",15,"bold"),
                                                       text_color="white")
        self.text_number_user.place(x=20,y=60)
        self.Entry_user_delete = customtkinter.CTkEntry(self.form_1,
                                                 width=140,
                                                 height=30,
                                                 border_width=1,
                                                 placeholder_text="number of the client"
                                                 )
        self.Entry_user_delete.place(y=60,x=240)
        
        
        self.name_user = customtkinter.CTkLabel(self.form_1,
                                                text="Enter the full name:",
                                                font=("Arial",15,"bold"),
                                                )
        self.name_user.place(x=20,y=120)
        self.Entry_name_user_delete = customtkinter.CTkEntry(self.form_1,
                                                 width=140,
                                                 height=30,
                                                 border_width=1,
                                                 placeholder_text="full name"
                                                 )
        self.Entry_name_user_delete.place(x=240,y=120)
        self.CNI = customtkinter.CTkLabel(self.form_1,
                                          text="enter CNI :",
                                          font=("Arial",15,"bold"))
        self.CNI.place(x=20,y=180)
        self.Entry_CNI_delete = customtkinter.CTkEntry(self.form_1,
                                                width=140,
                                                height=30,
                                                placeholder_text="numbre card national",
                                                border_width=1
                                                )
        self.Entry_CNI_delete.place(x=240,y=180)
        self.phone = customtkinter.CTkLabel(self.form_1,
                                            text="Enter phone numbre:",
                                            font=("Arial",15,"bold"))
        self.phone.place(x=20,y=240)
        self.Entry_phone_delete = customtkinter.CTkEntry(self.form_1,
                                                  width=140,
                                                  height=30,
                                                  border_width=1,
                                                  placeholder_text="+212600000001")
        self.Entry_phone_delete.place(y=240,x=240)
        self.gamil = customtkinter.CTkLabel(self.form_1,
                                            text="Enter city of client:",
                                            font=("Arial",15,"bold"))
        self.gamil.place(x=20,y=300)
        self.Entry_city_delete = customtkinter.CTkEntry(self.form_1,
                                                  width=140,
                                                  height=30,
                                                  placeholder_text="Guelmim",
                                                  border_width=1,)
        self.Entry_city_delete.place(x=240,y=300)
        self.date = customtkinter.CTkLabel(self.form_1,
                                           text="Numbre card of user:",
                                           font=("Arial",15,"bold"))
        self.date.place(x=20,y=360)
        self.Entry_number_card_delete = customtkinter.CTkEntry(self.form_1,
                                                 width=140,
                                                 height=30,
                                                 placeholder_text="XXXX-XXXX-XXXX-XXXX",
                                                 border_width=1)
        self.Entry_number_card_delete.place(x=240,y=360)


        self.btn_delete = customtkinter.CTkButton(self.form_1,
                                                  width=140,
                                                  height=28,
                                                  text="Delete",
                                                  font=("Arial",15,"bold"),
                                                  fg_color="red",
                                                  hover_color="#c20c0c",
                                                  command=self.delete_user)
        self.btn_delete.place(x=120,y=420)
        # self.scrolX.destroy()
        # self.scrolY.destroy()
        # self.form_3.destroy()
    def delete_user(self):

        #/////////////////////////////////////////////////////////////////////
            self.list_number.append(self.Entry_user_delete.get())
            self.list_number.append(self.Entry_name_user_delete.get())
            self.list_number.append(self.Entry_CNI_delete.get())
            self.list_number.append(self.Entry_phone_delete.get())
            self.list_number.append(self.Entry_city_delete.get())
            self.list_number.append(self.Entry_number_card_delete.get())
        
            detecte_line = 0
            with open("data_client.csv","r") as f_delete:
                csv_reader = csv.reader(f_delete)
                f_delete.__next__()
                try:
                    for self.find in csv_reader:
                        detecte_line += 1
                        
                        if  int(self.find[0]) != int(self.list_number[0]) :
                            
                            continue
                        else:
                            if int(self.find[0]) == int(self.list_number[0]) :
                                self.Entry_user_delete1 = customtkinter.CTkEntry(self.form_1,
                                                                        width=140,
                                                                        height=30,
                                                                        border_width=1,
                                                                        placeholder_text="correct",
                                                                        border_color="green"
                                                                        )
                                self.Entry_user_delete1.insert(0,self.list_number[0])
                                self.Entry_user_delete1.place(y=60,x=240)

                            if self.find[1] == self.list_number[1]:
                                self.Entry_name_user_delete1 = customtkinter.CTkEntry(self.form_1,
                                                                    width=140,
                                                                    height=30,
                                                                    border_width=1,
                                                                    placeholder_text="full name",
                                                                    border_color="green"
                                                                    )
                                self.Entry_name_user_delete1.insert(0,self.find[1])
                                self.Entry_name_user_delete1.place(x=240,y=120)
                            if self.find[1] != self.list_number[1]:
                                self.Entry_name_user_delete = customtkinter.CTkEntry(self.form_1,
                                                                    width=140,
                                                                    height=30,
                                                                    border_width=1,
                                                                    placeholder_text="wrong full name",
                                                                    border_color="red"
                                                                    )
                                self.Entry_name_user_delete.place(x=240,y=120)
                            if self.find[3] == self.list_number[2]:
                                self.Entry_CNI_delete1 = customtkinter.CTkEntry(self.form_1,
                                                                    width=140,
                                                                    height=30,
                                                                    placeholder_text="numbre card national",
                                                                    border_width=1,
                                                                    border_color="green",
                                                                    )
                                self.Entry_CNI_delete1.insert(0,self.find[3])
                                self.Entry_CNI_delete1.place(x=240,y=180)
                            if self.find[3] != self.list_number[2]:
                                self.Entry_CNI_delete = customtkinter.CTkEntry(self.form_1,
                                                                    width=140,
                                                                    height=30,
                                                                    placeholder_text="the number card is wrong",
                                                                    border_width=1,
                                                                    border_color="red",
                                                                    )
                                self.Entry_CNI_delete.place(x=240,y=180)
                            if self.find[5] == self.list_number[3]:
                                self.Entry_phone_delete1 = customtkinter.CTkEntry(self.form_1,
                                                                    width=140,
                                                                    height=30,
                                                                    border_width=1,
                                                                    placeholder_text="+212600000001",
                                                                    border_color="green")
                                self.Entry_phone_delete1.insert(0,self.find[5])
                                self.Entry_phone_delete1.place(y=240,x=240)
                            if self.find[5] != self.list_number[3]:
                                self.Entry_phone_delete = customtkinter.CTkEntry(self.form_1,
                                                                    width=140,
                                                                    height=30,
                                                                    border_width=1,
                                                                    placeholder_text="the phone is incorect",
                                                                    border_color="red")
                                self.Entry_phone_delete.place(y=240,x=240)
                            if self.find[6] == self.list_number[4]:
                                self.Entry_city_delete1 = customtkinter.CTkEntry(self.form_1,
                                                                    width=140,
                                                                    height=30,
                                                                    placeholder_text="Guelmim",
                                                                    border_width=1,
                                                                    border_color="green")
                                self.Entry_city_delete1.insert(0,self.find[6])
                                self.Entry_city_delete1.place(x=240,y=300)
                            if self.find[6] != self.list_number[4]:
                                self.Entry_city_delete = customtkinter.CTkEntry(self.form_1,
                                                                    width=140,
                                                                    height=30,
                                                                    placeholder_text="wrong city",
                                                                    border_width=1,
                                                                    border_color="red")
                                self.Entry_city_delete.place(x=240,y=300)
                            if self.find[8] == self.list_number[5]:
                                self.Entry_number_card_delete1 = customtkinter.CTkEntry(self.form_1,
                                                                        width=140,
                                                                        height=30,
                                                                        placeholder_text="XXXX-XXXX-XXXX-XXXX",
                                                                        border_width=1,
                                                                        border_color="green")
                                self.Entry_number_card_delete1.insert(0,self.find[8])
                                self.Entry_number_card_delete1.place(x=240,y=360)
                            if self.find[8] != self.list_number[5]:
                                self.Entry_number_card_delete = customtkinter.CTkEntry(self.form_1,
                                                                        width=140,
                                                                        height=30,
                                                                        placeholder_text="card bank number incorect!!",
                                                                        border_width=1,
                                                                        border_color="red")
                                self.Entry_number_card_delete.place(x=240,y=360)
                            if  int(self.find[0]) == int(self.list_number[0]) and self.find[1] == self.list_number[1] and self.find[3] == self.list_number[2] and self.find[5] == self.list_number[3] and self.find[6] == self.list_number[4] and self.find[8] == self.list_number[5]:
                                self.btn_delete = customtkinter.CTkButton(self.form_1,
                                                                        width=140,
                                                                        height=28,
                                                                        text="Delete",
                                                                        font=("Arial",15,"bold"),
                                                                        fg_color="red",
                                                                        hover_color="#c20c0c",
                                                                        command=self.delete_user,
                                                                        state=DISABLED)
                                self.btn_delete.place(x=120,y=420)
                                self.delete_line_file(detecte_line)
                                self.btn_go_home = customtkinter.CTkButton(self.form_1,
                                                                           text="go home",
                                                                           font=("Arial",15,"bold"),
                                                                           command=self.submit)
                                self.btn_go_home.place(x=1,y=2)

                                
                                
                except ValueError:
                    print("enter a integer number not string or float number")
            self.list_number.clear()
            
                    

    def delete_line_file(self,line):
        self.LR = line
        with open("data_client.csv") as file:
            read_line_file = file.readlines()
        if self.LR <= len(read_line_file):
            del read_line_file[self.LR]
            with open("data_client.csv","w",newline="") as update_file:
                for line_update in read_line_file:
                    update_file.write(line_update)
            messagebox.showinfo("Success", "User deleted.")
            
        else:
            messagebox.showerror("Error","user not found")
            

    
    def submit_check(self):
        # check for password if it's not right 
        if self.ask_text2.get() != str(compte_dictionary[-1]):
            self.ask_text2.destroy()
            
            self.ask_text2 = customtkinter.CTkEntry(self.windows,
                              width=180,height=30,border_color="red")
            self.ask_text2.place(x=290,y=150)
            self.text_wrong_code = customtkinter.CTkLabel(self.windows,
                                                          font=("Arial",10,"bold"),
                                                          text="red")
            self.text_wrong_code.place(x=500,y=150)
            self.text_wrong_code.destroy()


        # check for password if it's right 


        else:
            self.ask1.destroy()
            self.ask_text1.destroy()
            self.ask2.destroy()
            
            self.ask_text2.destroy()
            self.btn1.destroy()
            
            self.title = customtkinter.CTkLabel(self.windows,
                               text="you have been succesfull submitting",
                               pady=10,
                               padx=120,
                               font=("Arial",20,'bold')
                               )
            self.title.place(x=250,y=120)
            self.delete_img = PhotoImage(file="close.png")
            self.deletebtn = Button(self.windows,
                                    image=self.delete_img,
                                    border=0,
                                    
                                    command=self.destro)
            self.deletebtn.place(x=750,y=125)
            
            
            
            self.addbtn =customtkinter.CTkButton(self.windows,
                                 text="Add user",
                                 font=("Arial",15,"bold"),
                                 command=self.add_client,
                                 fg_color="green",
                                 hover_color="#046b04"
                                 )
            
            self.suprimerbtn =customtkinter.CTkButton(self.windows,
                                 text="Delete user",
                                 fg_color="red",
                                 font=("Arial",15,"bold"),
                                 hover_color="#c20c0c",
                                 command=self.suprimer_client,
                                 )
            self.suprimerbtn.place(x=400,y=200)
            self.addbtn.place(x=600,y=200)
            self.data_base_btn = customtkinter.CTkButton(self.windows,
                                                      text="show data",
                                                      font=("Arial",15,"bold"),
                                                      command=self.show_data_base)
            self.data_base_btn.place(x=500,y=400)
            

class client(agent):
    #show fram to client for sign in
    def login(self):
        self.voice = pygame.mixer.Sound(file="welcome.wav")
        self.voice.play()
        self.form_login = customtkinter.CTkFrame(self.windows,
                                                 width=360,
                                                 height=360,
                                                 corner_radius=16)
        self.form_login.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
        
        self.title1 = customtkinter.CTkLabel(self.form_login,
                                             text="sign in into your account",
                                             font=("Arial",15,"bold"))
        self.title1.place(x=80,y=20)
        self.label1= customtkinter.CTkLabel(self.form_login,
                                            text="Enter Full Name: ",
                                            font=("Arial",15,"bold"))
        self.label1.place(x=20,y=80)
        self.Entry_name_sign_in = customtkinter.CTkEntry(self.form_login,
                                                      width=140,
                                                      height=30,
                                                      placeholder_text="LAHCEN SKAIH")
        self.Entry_name_sign_in.place(y=80,x=170)
        self.label2 = customtkinter.CTkLabel(self.form_login,
                                             text="Enter password:",
                                             font=("Arial",15,"bold"))
        self.label2.place(x=20,y=180)
        self.Entry_code_sign_in = customtkinter.CTkEntry(self.form_login,
                                                         width=140,
                                                         height=30,
                                                         placeholder_text="2458",
                                                         show="*")
        self.Entry_code_sign_in.place(x=170,y=180)
        self.btn_sign_in = customtkinter.CTkButton(self.form_login,
                                                   text="sign in",
                                                   fg_color="green",
                                                   font=("Arial",15,"bold"),
                                                   height=30,
                                                   width=100,
                                                   hover_color="#046b04",
                                                   command=self.check_login)
        self.btn_sign_in.place(x=130,y=260)
    def check_login(self):
        with open("data_client.csv","r") as file:
                read_file = csv.reader(file)
            # try:    
                for self.ln in read_file:
               
                    if self.ln[1] == self.Entry_name_sign_in.get() :
                        self.Entry_name_sign_in.configure(border_color="green")
                        self.exact_name = self.ln[1]
                        
                        if self.ln[2] == self.Entry_code_sign_in.get():
                            self.exact_pwd = self.ln[2]
                            
                            self.btn_sign_in.configure(command=self.show_client_option)

                            self.Entry_code_sign_in.configure(border_color="green")
                            self.Entry_name_sign_in.configure(border_color="green")

                        if self.ln[2] != self.Entry_code_sign_in.get():
                            self.Entry_code_sign_in.configure(border_color="red")
                            
                            
                        
                    if self.ln[1] != self.Entry_name_sign_in.get() :
                        # self.Entry_name_sign_in.configure(border_color="purple")
                        continue
            # except :
            #     print("simple problem i will find it")
    def show_client_option(self):
        self.welcome = self.exact_name
        self.code = self.exact_pwd
        self.form_login.destroy()
        self.text.destroy()
        
        self.form_navbar = customtkinter.CTkFrame(self.windows,corner_radius=0,height=1000)
        self.form_navbar.place(x=0,y=0)
    #     #make welcome to the client with his name
        
        self.welcome_user = f"Hello {self.welcome}"
        self.show_welcome_text = customtkinter.CTkLabel(self.form_navbar,
                                                        text=self.welcome_user,
                                                        font=("Arial",15,"bold"),
                                                        )
        self.show_welcome_text.place(x=60,y=20)
        
        self.btn_account = customtkinter.CTkButton(self.form_navbar,
                                                               text="My Account",
                                                               font=("Arial",15,"bold"),
                                                               fg_color="transparent",
                                                               corner_radius=0,
                                                               hover_color=("gray70", "gray30"),
                                                               width=200,
                                                               height=60,
                                                               command=lambda:self.My_Account(self.code))
        self.btn_account.place(x=0,y=120)
        self.btn_withdraw = customtkinter.CTkButton(self.form_navbar,
                                                    text="Retirer",
                                                    fg_color="transparent",
                                                    corner_radius=0,
                                                    hover_color=("gray70", "gray30"),
                                                    font=("Arial",15,"bold"),
                                                    height=60,
                                                    width=200,
                                                    command=lambda:self.Withdraw(self.code))
        self.btn_withdraw.place(x=0,y=180)
        self.btn_deposit = customtkinter.CTkButton(self.form_navbar,
                                                   text="Deposer",
                                                   font=("Arial",15,"bold"),
                                                   corner_radius=0,
                                                   fg_color="transparent",
                                                   hover_color=("gray70", "gray30"),
                                                   width=200,
                                                   height=60,
                                                   command=lambda:self.Deposit(self.code))
        self.btn_deposit.place(x=0,y=240)
        self.btn_our_company = customtkinter.CTkButton(self.form_navbar,
                                                       text="Our Company",
                                                       fg_color="transparent",
                                                       corner_radius=0,
                                                       hover_color=("gray70", "gray30"),
                                                       font=("Arial",15,"bold"),
                                                       height=60,
                                                       width=200,
                                                       command=self.Our_Company)
        self.btn_our_company.place(x=0,y=300)
        self.frame_My_Account = customtkinter.CTkFrame(self.windows,
                                                       fg_color="transparent",
                                                       corner_radius=0,
                                                       width=700,height=500)
        self.frame_My_Account.place(x=280,y=150)
        self.fram_Deposit = customtkinter.CTkFrame(self.windows,
                                                   fg_color="transparent",
                                                   corner_radius=0,
                                                   width=550,
                                                   height=400)
        self.fram_withdraw = customtkinter.CTkFrame(self.windows,
                                                    fg_color="transparent",
                                                    corner_radius=0,
                                                    width=550,
                                                    height=400)
        self.fram_our_company = customtkinter.CTkFrame(self.windows,
                                                       fg_color="transparent",
                                                       corner_radius=0,
                                                       width=800,
                                                       height=600)
        
        self.chose_fram_by_name("Home")
    def chose_fram_by_name(self,name):
        self.name = name
        self.btn_account.configure(fg_color=("gray75", "gray25") if self.name == "Home" else "transparent")
        self.btn_deposit.configure(fg_color=("gray75", "gray25") if self.name == "deposit" else "transparent")
        self.btn_withdraw.configure(fg_color=("gray75", "gray25") if self.name == "withdraw" else "transparent")
        self.btn_our_company.configure(fg_color=("gray75", "gray25") if self.name == "our company" else "transparent")

        if self.name =="Home":
            self.frame_My_Account.place(x=320,y=80)
        else:
            self.frame_My_Account.place_forget()
        if self.name == "deposit":
            self.fram_Deposit.place(x=320,y=120)
        else:
            self.fram_Deposit.place_forget()
        if self.name == "withdraw":
            self.fram_withdraw.place(x=320,y=120)
        else:
            self.fram_withdraw.place_forget()
        if self.name == "our company":
            self.fram_our_company.place(x=260,y=80)
        else :
            self.fram_our_company.place_forget()


    def My_Account(self,code):
        self.secret_code = code
        self.chose_fram_by_name("Home")
        with open("data_client.csv","r") as read:
            self.reading = csv.reader(read)
            for row in self.reading:
                if row[2] == self.code:
                    self.label_name = customtkinter.CTkLabel(self.frame_My_Account,
                                                             text="your full name is :",
                                                             font=("Arial",15,"bold"),
                                                             )
                    self.label_name.place(x=20,y=60)
                    self.label_answear_name = customtkinter.CTkLabel(self.frame_My_Account,
                                                                     text=row[1],
                                                                     font=("Arial",15,"bold"))
                    self.label_answear_name.place(x=180,y=60)
                    self.label_card_Number = customtkinter.CTkLabel(self.frame_My_Account,
                                                                    text="Card Bank Number: ",
                                                                    font=("Arial",15,"bold"))
                    self.label_card_Number.place(x=20,y=170)
                    self.label_answear_card_number = customtkinter.CTkLabel(self.frame_My_Account,
                                                                            text=row[8],
                                                                            font=("Arial",15,"bold"))
                    self.label_answear_card_number.place(y=170,x=180)
                    self.label_code = customtkinter.CTkLabel(self.frame_My_Account,
                                                             font=("Arial",15,"bold"),
                                                             text="your code is :")
                    self.label_code.place(x=20,y=290)
                    self.label_answear_code = customtkinter.CTkLabel(self.frame_My_Account,
                                                                    text=row[2],
                                                                    font=("Arial",15,"bold"))
                    self.label_answear_code.place(y=290,x=180)
                    self.label_CNI = customtkinter.CTkLabel(self.frame_My_Account,
                                                            text="CNI :",
                                                            font=("Arial",15,"bold"))
                    self.label_CNI.place(x=20,y=400)
                    self.label_answear_cni = customtkinter.CTkLabel(self.frame_My_Account,
                                                                    text=row[3],
                                                                    font=("Arial",15,"bold"))
                    self.label_answear_cni.place(y=400,x=180)
                    self.label_Solde = customtkinter.CTkLabel(self.frame_My_Account,
                                                              text="Your Solde :",
                                                              font=("Arial",15,"bold"))
                    self.label_Solde.place(x=400,y=60)
                    self.answear_solde = customtkinter.CTkLabel(self.frame_My_Account,
                                                                text=row[7],
                                                                font=("Arial",15,"bold"))
                    self.answear_solde.place(y=60,x=560)
                    self.label_phone = customtkinter.CTkLabel(self.frame_My_Account,
                                                              text="Phone Number :",
                                                              font=("Arial",15,"bold"))
                    self.label_phone.place(x=400,y=170)
                    self.answear_phone =customtkinter.CTkLabel(self.frame_My_Account,
                                                               text=row[5],
                                                                font=("Arial",15,"bold"))
                    self.answear_phone.place(x=560,y=170)
                    self.label_gmail = customtkinter.CTkLabel(self.frame_My_Account,
                                                              text="Gmail:",
                                                              font=("Arial",15,"bold"))
                    self.label_gmail.place(x=400,y=290)
                    self.answear_gmail = customtkinter.CTkLabel(self.frame_My_Account,
                                                                text=row[4],
                                                                font=("Arial",15,"bold"))
                    self.answear_gmail.place(y=290,x=560)
                    self.label_city = customtkinter.CTkLabel(self.frame_My_Account,
                                                             text="City",
                                                             font=("Arial",15,"bold"))
                    self.label_city.place(y=400,x=400)
                    self.answear_city = customtkinter.CTkLabel(self.frame_My_Account,
                                                               text=row[6],
                                                               font=("Arial",15,"bold"))
                    self.answear_city.place(y=400,x=560)
            
    def Deposit(self,code):
        self.code_deposer = code
        self.chose_fram_by_name("deposit")
        
        #make text and button and entry for Deposit the Solde
        self.label_deposit = customtkinter.CTkLabel(self.fram_Deposit,
                                                    text="Enter Amount You want To Deposer:",
                                                    font=("Arial",15,"bold"))
        self.label_deposit.place(x=40,y=120)
        self.Entry_deposit = customtkinter.CTkEntry(self.fram_Deposit,
                                                    width=120,
                                                    height=35,
                                                    font=("Arial",20,"bold"))
        self.Entry_deposit.place(y=120,x=340)
        self.btn_deposer = customtkinter.CTkButton(self.fram_Deposit,
                                                   text="Deposer",
                                                   fg_color="green",
                                                   font=("Arial",15,"bold"),
                                                   height=35,
                                                   width=100,
                                                   hover_color="#046b04",
                                                   command=lambda:self.check_deposer(self.code_deposer))
        self.btn_deposer.place(x=180,y=180)
    
    def check_deposer(self,code):
        self.checking = code
        self.somme_solde = 0
        
        if self.Entry_deposit.get().isdigit():
            if int(self.Entry_deposit.get()) < 0 :
                self.Entry_deposit.configure(border_color="red")

                self.Entry_deposit.delete(0,"end")
            else:
                self.Entry_deposit.configure(border_color="green")
                
                with open("data_client.csv","r") as f1 , open("data_save.csv","w",newline="") as f2:
                    f1_read = csv.reader(f1)
                    f2_write = csv.writer(f2)
                    

                    for line in f1_read:
                        if line[2] == self.checking:
                            for number in line[7]:
                                if number.isdigit():
                                    self.somme_solde = int(str(self.somme_solde) + str(number))
                                else:
                                    continue
                            self.new_solde = self.somme_solde + int(self.Entry_deposit.get())
                            
                            line[7]  = f"{self.new_solde} "
                            
                        f2_write.writerow(line)
                with open("data_save.csv" , "r") as f_read ,open("data_client.csv","w",newline="") as f_write:
                    fr1 = csv.reader(f_read)
                    fr2 = csv.writer(f_write)
                    for ln in fr1:
                        if ln[2] == self.checking:
                            messagebox.showinfo("succes",f"your solde is {ln[7]}")
                        fr2.writerow(ln)

        else:
            self.Entry_deposit.configure(border_color="red")
            self.Entry_deposit.delete(0,"end")
                

    def Our_Company(self):
        self.chose_fram_by_name("our company")
        self.txt = """The application made by Lahcen Skaih in the city of Guelmim\n\nis a banking application with two main options: Agent and Client.\n\nFor agents, the application allows them to create new accounts for clients \n\nand change the password of existing accounts. They can also access client data,\n\nsuch as personal information and account balance, and deposit money into clientaccounts.\n\nAdditionally, agents have the ability to delete client accounts from the system.\n\nOn the other hand, for clients, the application offers the ability to sign in to their\n\naccounts and perform various transactions, such as withdrawing and depositing money.\n\nThey can also view their personal information, such as name and address,\n\nas well as their account balance.\n\nOverall, this banking application provides a convenient and secure way for agents\n\nand clients to manage their banking needs from the comfort of their own devices.\n\n """
        self.label_about_us = customtkinter.CTkLabel(self.fram_our_company,
                                                     font=("Arial",15,"bold"),
                                                    text=self.txt,
                                                            )
        self.label_about_us.place(x=20,y=20)
        self.label_text = customtkinter.CTkLabel(self.fram_our_company,
                                                 text="for contact :",
                                                 font=("Arial",15,"bold"))
        
        self.label_contact = customtkinter.CTkLabel(self.fram_our_company,
                                                    text="lahcenenligne@gmail.com",
                                                    font=("Arial",15,"bold"),
                                                    text_color="#6fa8dc")
        self.label_text.place(x=40,y=480)
        self.label_contact.place(y=480,x=160)
        
      
    def Withdraw(self,code):

        self.code_withdraw = code
        self.chose_fram_by_name("withdraw")

        self.label_withdraw = customtkinter.CTkLabel(self.fram_withdraw,
                                                     text="Enter The Amount You Want To retirer:",
                                                     font=("Arial",15,"bold"))
        self.label_withdraw.place(x=40,y=120)
        self.Entry_withdraw = customtkinter.CTkEntry(self.fram_withdraw,
                                                     font=("Arial",15,"bold"),
                                                     width=120,
                                                     height=35)
        self.Entry_withdraw.place(y=120,x=360)
        self.btn_withdrawing = customtkinter.CTkButton(self.fram_withdraw,
                                                       text="Withdraw",
                                                       font=("Arial",15,"bold"),
                                                       fg_color="red",
                                                       height=35,
                                                       width=100,
                                                       hover_color="#c20c0c",
                                                       command=lambda:self.check_withdraw(self.code_withdraw))
        self.btn_withdrawing.place(y=180,x=180)
        
    def check_withdraw(self,code):
        self.check_code = code
        self.detect_solde = 0
        if self.Entry_withdraw.get().isdigit():
            if int(self.Entry_withdraw.get()) >= 0:
                with open("data_client.csv","r") as read1 ,open("data_save.csv","w",newline="") as write1:
                    reader1 = csv.reader(read1)
                    writer1 = csv.writer(write1)
                    for row_W in reader1:
                        if row_W[2] == self.check_code:
                            for digt in row_W[7]:
                                if digt.isdigit():
                                    self.detect_solde = int(str(self.detect_solde) + str(digt))
                                else:
                                    continue
                            if self.detect_solde >= int(self.Entry_withdraw.get()):
                                self.new_sold = self.detect_solde - int(self.Entry_withdraw.get())
                                self.Entry_withdraw.configure(border_color="green")
                                self.Entry_withdraw.delete(0,"end")
                                row_W[7] = f"{self.new_sold} "
                            else:
                                self.Entry_withdraw.configure(border_color="red")
                                self.Entry_withdraw.delete(0,"end")
                        writer1.writerow(row_W)
                with open("data_save.csv","r") as read2,open("data_client.csv","w",newline="") as write2:
                    reader2 = csv.reader(read2)
                    writer2 = csv.writer(write2)
                    for row_w2 in reader2:
                        if row_w2[2] == self.check_code:
                            messagebox.showinfo("succes",f"your solde is {row_w2[7]}")
                        writer2.writerow(row_w2)
            else:

                self.Entry_withdraw.delete(0,"end")
        else:
            self.Entry_withdraw.delete(0,"end")
            

class choic(client):

    def __init__(self):
        show_interface.__init__(self)

    def choise(self):
        

        self.ask = customtkinter.CTkLabel(self.windows,
                         text="are you agent or client: ",
                         font=("Arial",
                               20,
                               "bold"))
        self.ask.place(x=20,y=100)
        self.ask_text = customtkinter.CTkEntry(self.windows,
                              width=180,height=30)
        self.ask_text.place(x=300,y=100)
        self.btn =customtkinter.CTkButton(self.windows,
                     text="next-->",
                     border_width=1,
                     command=self.agent_client
                     )
        self.btn.place(x=180,y=150)
        return ""
        # simple problem i will find it
    def agent_client(self):

        if self.ask_text.get() == "agent":
            
            self.ask_text.destroy()
            self.ask.destroy()
            self.btn.destroy()
            self.check_agent()
            return True

        elif self.ask_text.get() == "client":
            self.ask_text.destroy()
            self.ask.destroy()
            self.btn.destroy()
            self.login()
        else:
            self.ask_text.destroy()
            self.ask_text = customtkinter.CTkEntry(self.windows,
                              width=180,height=30,
                              border_color="red")
            self.ask_text.place(x=300,y=100)

si = choic()

si.choise()

si.interface()