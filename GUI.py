from tkinter import *
import Client
import uuid
import tkinter as tk
from threading import Thread


MAC_ADDRESS = hex(uuid.getnode() - 1)


class GUI(Thread):
    def __init__(self, gui_object):
        super().__init__()
        self.client = Client.Client(MAC_ADDRESS, 68, self)
        self.left_frame1 = Frame(gui_object)
        self.left_frame2 = Frame(gui_object)
        self.bottom_frame = Frame(gui_object)
        self.right_frame = Frame(gui_object)
        self.discover = Button(self.bottom_frame, text="Discover", command=self.client.discover)
        self.request = Button(self.bottom_frame, text="Request", command=self.client.request, state=tk.DISABLED)
        self.decline = Button(self.bottom_frame, text="Decline", command=self.client.decline, state=tk.DISABLED)
        self.release = Button(self.bottom_frame, text="Release", command=self.client.release, state=tk.DISABLED)
        self.inform = Button(self.bottom_frame, text="Inform", command=self.client.inform, state=tk.DISABLED)
        self.display = Button(self.bottom_frame, text="Display", command=self.client.display, state=tk.DISABLED)
        self.REQUESTED_IP = IntVar()
        self.SUBNET_MASK = IntVar()
        self.TIME_OFFSET = IntVar()
        self.TIME_SERVER = IntVar()
        self.HOST_NAME = IntVar()
        self.PARAMETER_REQUEST_LIST = IntVar()
        self.DOMAIN_NAME = IntVar()
        self.LEASE_TIME = IntVar()
        self.RENEWAL_TIME = IntVar()
        self.REBINDING_TIME = IntVar()
        self.DNS = IntVar()
        self.option11 = 1
        self.option12 = 1
        self.text = Text(self.right_frame, width=70, height=20, background='black', foreground='mediumspringgreen')

    def run(self):
        self.left_frame1.grid(row=0, column=0)
        self.left_frame2.grid(row=0, column=1)
        self.bottom_frame.grid(row=1, column=0, columnspan=3)
        self.right_frame.grid(row=0, column=2)

        o1 = Checkbutton(self.left_frame1, variable=self.REQUESTED_IP, height=2, width=6)
        o2 = Checkbutton(self.left_frame1, variable=self.SUBNET_MASK, height=2, width=6)
        o3 = Checkbutton(self.left_frame1, variable=self.TIME_OFFSET, height=2, width=6)
        o4 = Checkbutton(self.left_frame1, variable=self.TIME_SERVER, height=2, width=6)
        o5 = Checkbutton(self.left_frame1, variable=self.HOST_NAME, height=2, width=6)

        o6 = Checkbutton(self.left_frame2, variable=self.PARAMETER_REQUEST_LIST, height=2, width=6)
        o7 = Checkbutton(self.left_frame2, variable=self.DOMAIN_NAME, height=2, width=6)
        o8 = Checkbutton(self.left_frame2, variable=self.LEASE_TIME, height=2, width=6)
        o9 = Checkbutton(self.left_frame2, variable=self.RENEWAL_TIME, height=2, width=6)
        o10 = Checkbutton(self.left_frame2, variable=self.REBINDING_TIME, height=2, width=6)
        o11 = Checkbutton(self.left_frame1, variable=self.option11, height=2, width=6, state=tk.DISABLED)
        o11.select()
        o12 = Checkbutton(self.left_frame2, variable=self.option12, height=2, width=6, state=tk.DISABLED)
        o12.select()
        o13 = Checkbutton(self.left_frame1, variable=self.DNS, height=2, width=6)

        o1_label = Label(self.left_frame1, text="Option 50: Requested IP")
        o2_label = Label(self.left_frame1, text="Option  1: Subnet Mask")
        o3_label = Label(self.left_frame1, text="Option  2: Time Offset")
        o4_label = Label(self.left_frame1, text="Option  4: Time Server")
        o5_label = Label(self.left_frame1, text="Option 12: Host Name")

        o6_label = Label(self.left_frame2, text="Option 55: Parameter Request List")
        o7_label = Label(self.left_frame2, text="Option 15: Domain Name")
        o8_label = Label(self.left_frame2, text="Option 51: Ip Address Lease Time")
        o9_label = Label(self.left_frame2, text="Option 58: Renewal Time Value")
        o10_label = Label(self.left_frame2, text="Option 59: Rebinding Time Value")
        o11_label = Label(self.left_frame1, text="Option 53: Message Type")
        o12_label = Label(self.left_frame2, text="Option 255: End")
        o13_label = Label(self.left_frame1, text="Option 6: DNS")

        o1.grid(row=1, column=0)
        o2.grid(row=3, column=0)
        o3.grid(row=5, column=0)
        o4.grid(row=7, column=0)
        o5.grid(row=9, column=0)
        o11.grid(row=13, column=0)
        o13.grid(row=11, column=0)

        o6.grid(row=1, column=0)
        o7.grid(row=3, column=0)
        o8.grid(row=5, column=0)
        o9.grid(row=7, column=0)
        o10.grid(row=9, column=0)
        o12.grid(row=13, column=0)

        o1_label.grid(row=0, column=0)
        o2_label.grid(row=2, column=0)
        o3_label.grid(row=4, column=0)
        o4_label.grid(row=6, column=0)
        o5_label.grid(row=8, column=0)
        o11_label.grid(row=12, column=0)

        o6_label.grid(row=0, column=0)
        o7_label.grid(row=2, column=0)
        o8_label.grid(row=4, column=0)
        o9_label.grid(row=6, column=0)
        o10_label.grid(row=8, column=0)
        o12_label.grid(row=12, column=0)
        o13_label.grid(row=10, column=0)

        self.text.pack(side=RIGHT)
        self.discover.grid(row=0, column=0, padx=5, pady=5)
        self.request.grid(row=0, column=1, padx=5, pady=5)
        self.decline.grid(row=0, column=2, padx=5, pady=5)
        self.release.grid(row=0, column=3, padx=5, pady=5)
        self.inform.grid(row=0, column=4, padx=5, pady=5)
        self.display.grid(row=0, column=5, padx=5, pady=5)

    def setText(self, info):
        self.text.insert(END, str(info))

    def deleteText(self):
        self.text.delete('1.0', END)
