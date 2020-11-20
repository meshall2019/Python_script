import smtplib
"""
most imprtent note:
you must to enable the access to less secure apps before you write your sender email
------------------------------------------------------------------------------------
***************************************************
note:
Script has been MODIFIED by Meshal AL-Rhsdan
MY job:
- You can add more then Receiver
-You can sending the emil as many times as you want
*****************************************************
"""
receivers_Emils=[]#array for the Receivers's Emils
sender = input(" Enter your Email : ")
password = input("Enter the Password : ")
receivers = input("Enter your Receiver : ")
receivers_Emils.append(receivers)#adding the emil to the array
while True:
    add_emil=input("Do you want add more recivers..? yes or no")
    if add_emil=='yes':
        receivers = input("Enter your Receiver : ")
        receivers_Emils.append(receivers)
    else:
        break
message =input ("Enter your Message : ")
num_Emils=int(input("How many numbers of emils do you want to send ..? "))#asking for the numbers of emils
try:
    for emil in receivers_Emils:#for each emil in the receivers_Emils array
        for n in range(num_Emils):# for Repeting sending the emil

         server = smtplib.SMTP_SSL('smtp.gmail.com', 465)# port of gmail for making the conection
         server.login(sender,password)
         server.sendmail( sender ,emil, message)
         server.quit()
         print(' sent Successfully')
        print("completed send to",emil)
    print("****thank you*****")
except:
        print(' there is error ')


