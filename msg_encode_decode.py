from email import message

from tkinter import*
from tkinter import messagebox
import base64


import requests
import os


def decrypt():
    
    password=code.get()

    if password=="1234":
        screen1=Toplevel(root)
        screen1.title("Decryption")
        screen1.geometry("260x300")
        screen1.config(bg="deepskyblue1")

        message=textarea.get(1.0 , END)
        decode_message=message.encode("ascii")
        base64_byte=base64.b64decode(decode_message)
        decrypt=base64_byte.decode("ascii")



        Label(screen1 ,text="DECRYPT" , font="lucida" ,fg="white" ,bg="deepskyblue1" , width=25 ,bd=3).grid(row=0 ,column=0 ,pady=3)
        textarea2=Text(screen1, font="lucida ", bg="white" ,relief=SUNKEN ,wrap=WORD ,bd=2 , width=25 , height=11)
        textarea2.grid(row=1 ,column=0 , pady=3)

        textarea2.insert(END ,decrypt)


    elif password=="":
        messagebox.showerror("decryption" , "Input Password")

    elif password!="1234":
        messagebox.showerror("decryption" , "Invalid Password")    



 

    

def encrypt():
    password=code.get()

    if password=="1234":
        screen=Toplevel(root)
        screen.title("Encryption")
        screen.config(bg="lightgreen")
        screen.geometry("260x300")
        
    
        message=textarea.get(1.0,END)
        encode_msg=message.encode("ascii")
        base64_byte=base64.b64encode(encode_msg)
        encrypt=base64_byte.decode("ascii")


        Label( screen ,text="ENCRYPT" , font="lucida" ,fg="white" ,bg="deepskyblue1" , width=25 ,bd=3).grid(row=0 ,column=0 ,pady=3)
        textarea2=Text(screen , font="lucida ", bg="white" ,relief=SUNKEN ,wrap=WORD ,bd=2 , width=25 , height=11)
        textarea2.grid(row=1 ,column=0 , pady=3)

        textarea2.insert(END ,encrypt)

    elif password=="":
        messagebox.showerror("encryption " , "Input password")

    elif password!="1234":
        messagebox.showerror("encryption" , " Invalid Password")    





def main_root():

  global textarea
  global code
  global root

root=Tk()

root.geometry("450x450")
root.config(bg="skyblue")

root.title("Message-Encode-Decode")


def reset():
    code.set("")

    textarea.delete(1.0 , END) 



#Encryption and description
Label(text="Enter text for ecryption and decrytion" ,  fg="black" , font="lucida 12 bold" ,relief=SUNKEN  , bd=3 , width=40).grid( pady=1, row=0 , column=0)

textarea=Text(root,  fg="black" ,width=55  , height=11 , bd=3 )
textarea.grid(row=3, column=0 , pady=5)

#Secret key
Label(text="Enter Secret Key for encryption and descryption ",fg="black",font="lucida 12 bold" ,relief=SUNKEN ,bd=3).grid(pady=1)

code=StringVar()
entrykey=Entry(root , textvariable=code, font="flat 18 bold" , width=26 , show="*" )
entrykey.grid(padx=1 , pady=4)

btnencrypt=Button(root ,text="ENCRYPTION "  ,fg="black" , font="Flat 10 bold", bg="green" ,relief=RAISED , bd=5 , command=encrypt)
btnencrypt.grid(row=7 , column=0 , padx=16 , pady=2 )


btndiscription=Button(root ,text="DESCRYPTION "  ,fg="black" , font="Flat 10 bold", bg="red" , relief=RAISED , bd=5 , command=decrypt) 
btndiscription.grid(row=8 , column=0 )


nextbtn=Button(root , text="RESET" , fg="white" , bg="deepskyblue4" , font=" flat 18  bold" , relief=RAISED , bd=4 , width=24 , command=reset )
nextbtn.grid(pady=3)











root.mainloop()
