from tkinter import *
from tkinter import messagebox
import base64



win = Tk()
win.geometry("400x400")
win.title("ENCODE AND DECODE")
win.config(bg="light blue")

#DEFINING FUNCTIONS:

def encryption():
    pas = endec.get()
    if pas == "abcd":
        newscreen = Toplevel(win) #Toplevel is used for new screen pop up
        newscreen.geometry("400x250")#for new screen for encoding
        newscreen.title("ENCRYPTION PAGE")
        newscreen.config(bg = "red")
        
        msg = text1.get(1.0, END) #first line zero character to the end
        msg_encodding = msg.encode("utf-8") #for encodding message
        base64_use = base64.b64encode(msg_encodding) #most important line for encoding use encode for decoding use decode.
        encryption = base64_use.decode("utf-8")
        
        # Label and place for newscreen
        lab1 = Label(newscreen, text="Encrypted Successfully!!", font=("Time New Roman", 12, "bold"), bg= "green")
        lab1.place(x = 5, y = 10)
        txt = Text(newscreen, font="30", bd= 4, wrap=WORD)
        txt.place(x = 10, y = 60, height= 150, width= 300)
        txt.insert(END, encryption)
        
    elif(pas == ""):
        messagebox.showerror("ALERT", "EMPTY SECRET KEY!")
        
    elif(pas!= "abcd"):
        messagebox.showwarning("WARNING", "INCORRECT SECRET KEY.")
        
        
#Functions for decryption:

def decryption():
    
        pas = endec.get()
        if pas == "abcd":
            newscreen1 = Toplevel(win) #Toplevel is used for new screen pop up
            newscreen1.geometry("400x250")#for new screen for decode
            newscreen1.title("ENCRYPTION PAGE")
            newscreen1.config(bg = "green")
            
            # main lines for encodding
            msg = text1.get(1.0, END) #first line zero character to the end
            msg_encodding = msg.encode("utf-8") #for encodding message
            base64_use = base64.b64decode(msg_encodding)
            encryption = base64_use.decode("utf-8")
            
            # Label and place for newscreen
            lab1 = Label(newscreen1, text="Your Message is Decrypted!!", font=("Time New Roman", 10, "bold"), bg= "green")
            lab1.place(x = 5, y = 10)
            txt = Text(newscreen1, font="30", bd= 4, wrap=WORD)
            txt.place(x = 10, y = 60, height= 150, width= 300)
            txt.insert(END, encryption)
        
        elif(pas == ""):
            messagebox.showerror("ALERT", "EMPTY SECRET KEY!")
            
        elif(pas!= "abcd"):
            messagebox.showwarning("WARNING", "INCORRECT SECRET KEY.")
        elif(text1 == ""):
            messagebox.showerror("ERROR", "Please enter Something")
            
    
# Function for reset       
def reset():
    text1.delete(1.0, END)
    endec.set("")
           

#heading Label and Place
heading_Label = Label(win, text="Encryption And Decryption", font=("Times New Roman", 15, "bold"))
heading_Label.place(x = 50, y = 35, width= 300)

#For text areas
text1 = Text(font=("Times New Roman", 12))
text1.place(x = 17, y = 80, height= 100, width= 370)

#Label and Palce
heading_Labe2 = Label(win, text="Enter Your Encrypted Code", font=("Times New Roman", 12,"bold"), fg="purple")
heading_Labe2.place(x = 105, y = 200)

#For text Areas
Label2 = Label(win, text="Enter Encrypted Code", font=("Times New Roman" ,17, "bold"))
Label2.place(x = 113, y = 238, width= 160, height= 25)

#For Entry in the blank space
endec = StringVar()
Entry( textvariable=endec, bd=4, font="20", show="*").place(x = 113, y = 238, width= 160, height= 25)

#Buttons
Buttons = Button(win, text="ENCODE", font=("Arial", 13, "bold"), bg="red", bd= 4, command= encryption)
Buttons.place(x = 55, y = 290, height= 30)

Buttons1 = Button(win, text="DECODE", font=("Arial", 13, "bold"), bg="green", bd= 4, command=decryption )
Buttons1.place(x = 220, y = 289, height= 30)

Buttons3 = Button(win, text="RESET", font=("Arial", 13, "bold"), bg="YELLOW", bd= 4, command= reset )
Buttons3.place(x = 90, y = 340, height= 30, width= 190)


win.mainloop()
