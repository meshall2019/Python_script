import smtplib
from tkinter import *
from tkinter import messagebox
"""
must imprtent note:
you must to enable the access to less secure apps before you write your sender email
------------------------------------------------------------------------------------
***************************************************
note:
Script It has been MODIFIED by Meshal AL-Rhsdan
MY job:
- You can add more then Receiver
-You can sending the emil as many times as you want
- You can sending the emil by using GUI
*****************************************************
"""

window = Tk()
window.title("Sending Emil")
receivers_Emils = []  # array for the Receivers's Emils

enter_emil=Label(window,text="Enter your Emil: ")
enter_emil.pack()
sender_emil=Entry(window,width=20)
sender_emil.pack()

enter_passwd=Label(window,text="Enter your password: ")
enter_passwd.pack()
sender_passwd=Entry(window,width=20)
sender_passwd.pack()

enter_receiver=Label(window,text="Enter your Receiver: ")
enter_receiver.pack()
receiver_emil=Entry(window,width=20,)
receiver_emil.pack()


def add_receiver():
       receivers_Emils.append(receiver_emil.get())  # adding the emil to the array

add_receiver=Button(window,width=13,text="add a receiver",bg="#ff9999",command=add_receiver)
add_receiver.pack()


def delet():
    receiver_emil.delete(-1, END)


delet_receiver = Button(window, width=6, text="clear", bg="#ff9999", command=delet)
delet_receiver.pack()

massege=Label(window,text="Enter your massege: ")
massege.pack()
massege_entry=Entry(window,width=20)
massege_entry.pack()

number_massege=Label(window,text="Enter the number of masseges: ")
number_massege.pack()
number_massege_entry=Entry(window,width=20)
number_massege_entry.pack()

def send():
    sender1=sender_emil.get()
    passwd1=sender_passwd.get()
    message1=massege_entry.get()
    number_massege1=number_massege_entry.get()
    int_number_masseg1=int(number_massege1)
    try:

     for emil in receivers_Emils:  # for each emil the the receivers_Emils array
            for n in range(int_number_masseg1):  # for Repeting sending the emil

                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # port of gmail for making the conection
                server.login(sender1, passwd1)
                server.sendmail(sender1, emil, message1)
                server.quit()
                after_send.configure(text=str(n)+" messages have been send to "+emil)


    except:
        after_send.configure(text=" Error")
button_send=Button(window,width=25,text="Send the masseg",bg="#ff9999",command=send)
button_send.pack()

after_send=Label(window,)
after_send.pack()

window.mainloop()





