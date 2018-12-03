# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 21:16:01 2018

@author: User
"""

import tkinter as tk
from tkinter import scrolledtext
class Window():
    def __init__(self, title):
        self.root = tk.Tk()
        self.title = title
        self.root.title(title)
        

class ChatWindow(Window):
    
    def __init__(self, title):        
        super().__init__(title)
        self.messages_list = None
        self.logins_list = None
        self.entry = None
        self.send_button = None
        self.send_func = None        
        self.exit_button = None
        self.target = ''
        self.build_window()
        
    def set_send_function(self,function):
        self.send_func = function
        
    def build_window(self):
        # Size config
        self.root.geometry('750x500')
        self.root.minsize(600, 400)
        # Frames config
        main_frame = tk.Frame(self.root)
        main_frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        # List of messages
        frame00 = tk.Frame(main_frame)
        frame00.grid(column=0, row=0, rowspan=2, sticky=tk.N + tk.S + tk.W + tk.E)
        # List of logins
        frame01 = tk.Frame(main_frame)
        frame01.grid(column=1, row=0, rowspan=3, sticky=tk.N + tk.S + tk.W + tk.E)
        # Message entry
        frame02 = tk.Frame(main_frame)
        frame02.grid(column=0, row=2, columnspan=1, sticky=tk.N + tk.S + tk.W + tk.E)
        # Buttons
        frame03 = tk.Frame(main_frame)
        frame03.grid(column=0, row=3, columnspan=2, sticky=tk.N + tk.S + tk.W + tk.E)
        main_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=8)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        # ScrolledText widget for displaying messages
        self.messages_list = scrolledtext.ScrolledText(frame00, wrap='word')
        self.messages_list.insert(tk.END, 'Welcome to Python Chat\n')
        self.messages_list.configure(state='disabled')

        # Listbox widget for displaying active users and selecting them
        self.logins_list = tk.Listbox(frame01, selectmode=tk.SINGLE,
                                      exportselection=False)

        # Entry widget for typing messages in
        self.entry = tk.Text(frame02)
        self.entry.focus_set()
        self.entry.bind('<Return>')

        # Button widget for sending messages
        self.send_button = tk.Button(frame03, text='Send')
        self.send_button.bind('<Button-1>',self.send_msg)

        # Positioning widgets in frame
        self.messages_list.pack(fill=tk.BOTH, expand=tk.YES)
        self.logins_list.pack(fill=tk.BOTH, expand=tk.YES)
        self.entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        self.send_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
#        self.exit_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

        # Protocol for closing window using 'x' button
        self.root.protocol("WM_DELETE_WINDOW")
    
    def send_msg(self,send_function):
        if self.send_func is None:
            print("send_function is null")
        else:
            try:
                msg = self.entry.get(1.0,tk.END)
                if not msg.isspace():
                    #self.messages_list.insert(1.0,msg)
                    self.send(msg)
                    msg = self.entry.get(1.0,tk.END)
                    self.entry.delete(1.0,tk.END)
            except:
                pass
    
    def view_new_msg(self,new_msg):
        self.messages_list.configure(state='normal')        
        self.messages_list.insert(1.0,new_msg)
        self.messages_list.configure(state='disabled')
    
     

c= ChatWindow('chat')

c.root.mainloop()