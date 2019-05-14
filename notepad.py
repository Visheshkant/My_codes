from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import smtplib

saved = False

def newFile():
    root.title("Untitled - PyBook")
    text.delete(1.0, END)

def save():
        f = asksaveasfilename(initialfile='Unknown.txt', 
                                        defaultextension=".txt", 
                                        filetypes=[("All Files","*.*"), 
                                            ("Text Documents","*.txt")])
        global saved
        saved = True
        
        if f == "" :
            f = None
        else:
            file = open(f,"w") 
            file.write(text.get(0.0,END)) 
            file.close()
            root.title(os.path.basename(f) +" -  "+ os.getcwd())

def openFile():
    f = askopenfilename(defaultextension=".txt", 
                                  filetypes=[("All Files","*.*"), 
                                      ("Python Documents","*.py")])
    if f == "" :
        f=None
    else:
        root.title(os.path.basename(f) +" -  "+ os.getcwd())
        text.delete(1.0, END)
        file = open(f,'r')
        text.insert(1.0, file.read())
        file.close()

def cut():
   text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<paste>>")

def showAbout():
   showinfo("PyBook", "Python Version : 3.6.5 Notepad Version : 3.6.5")

def monolitik():
    text.configure(background='#262626', fg='white', insertbackground='white')

def light():
    text.configure(background='white smoke', fg='black', insertbackground='black')

def zoom_plus():
    text.configure(font=('monospace', 30))

def zoom_minus():
    text.configure(font=('monospace', 10))

def default():
    text.configure(font=('monospace', 16), fg='black')

def clear():
    ans = askquestion("Notice", "It won't save the text on your PyBook")
    if ans == "yes" :
         text.delete("1.0", END)

def highlighter(event):
    highlightWords = {'if': 'orange', 'else': 'orange', 'none': 'orange', 'false': 'orange', 'true': 'orange', 'and': 'orange', 'as': 'orange', 'assert': 'orange',
                      'break': 'orange', 'class': 'orange', 'continue': 'orange', 'def': 'orange', 'del': 'orange', 'elif': 'orange', 'except': 'orange', 'for': 'orange'}
    for key, color in highlightWords.items():
        start_Index = "1.0"
        while True:
            start_Index = text.search(key, start_Index, END)                  #for the starting point
            if start_Index:
                end_Index = text.index("%s + %dc" %(start_Index, len(key)))   #for the ending point
                text.tag_add(key, start_Index, end_Index)
                text.tag_config(key, foreground=color)
                start_Index = end_Index
            else:
                break

def send_mail():
    top = Toplevel()
    frame = Frame(top)
    frame.pack(side = LEFT)
    
    sender_mail = Label(frame, text = "Your Mail : ")
    sender_mail_password = Label(frame, text = "Password : ")
    receiver_mail = Label(frame, text = "Receiver's Mail : ")
    sender_mail.grid(row = 0, column = 0, sticky = W)
    sender_mail_password.grid(row = 1, column = 0,sticky = W)
    receiver_mail.grid(row = 2, column = 0,sticky = W)

    sender_mail_var = StringVar()
    sender_mail_entrybox = Entry(frame, width = 16, textvariable =sender_mail_var )
    sender_mail_entrybox.grid(row = 0, column = 1, sticky = W)

    sender_mail_password_var = StringVar()
    sender_mail_password_entrybox = Entry(frame, width = 16, textvariable =sender_mail_password_var )
    sender_mail_password_entrybox.grid(row = 1, column = 1, sticky = W)

    receiver_mail_var = StringVar()
    receiver_mail_entrybox = Entry(frame, width = 16, textvariable =receiver_mail_var )
    receiver_mail_entrybox.grid(row = 2, column = 1, sticky = W)
    
    def sendmail():
        global saved
        mail_sender = sender_mail_var.get()
        mail_sender_password = sender_mail_password_var.get()
        mail_receiver = receiver_mail_var.get()
        if saved == True :
            mail = text.get(1.0, END)
            connection = smtplib.SMTP('smtp.gmail.com', 587)
            connection.ehlo()
            connection.starttls()
            connection.login(mail_sender, mail_sender_password)
            connection.sendmail(mail_sender, mail_receiver, mail)
        else:
            ans = askquestion("Warning", "It semm that your file is not saved!\nWould you like to save it?")
            if ans == "yes" :
                f = asksaveasfilename(initialfile='Unknown.txt', 
                                        defaultextension=".txt", 
                                        filetypes=[("All Files","*.*"), 
                                            ("Text Documents","*.txt")])
                saved = True
        
                if f == "" :
                    f = None
                else:
                    file = open(f,"w") 
                    file.write(text.get(0.0,END)) 
                    file.close()
                    root.title(os.path.basename(f) +" -  "+ os.getcwd())

            
    send_btn = Button(frame, text = "Send", width = 13, command = sendmail)
    send_btn.grid(row = 4, column = 0, sticky = W)

# *************************  FRONT-END  **************************

root = Tk()
root.title("Untitled - PyBook")
root.minsize(width=500, height=500)
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)
text = Text(root, wrap = WORD, yscrollcommand=scrollbar.set)
text.focus()
contents = text.get(1.0, END)  # --->> To get content of the  text widget
text.config(background="white", font=('sans-serif', 16))
text.pack(expand = True, fill = BOTH)  # --->> For the default window size 
scrollbar.config(command = text.yview)
text.bind("<KeyRelease>", highlighter)

# **************************** FILE MENU *********************************

menubar = Menu(root)
root.config(menu = menubar)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=save)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.destroy)

# ******************************* EDIT MENU *******************************

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu = editmenu)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)
editmenu.add_command(label="Clear All", command=clear)

# ******************************* HELP MENU *******************************

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu = helpmenu)
helpmenu.add_command(label="About Notepad", command=showAbout)

# ******************************* PREFERENCE MENU *****************************

preferencemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = 'Preferences', menu = preferencemenu)

thememenu = Menu(preferencemenu, tearoff=0)
preferencemenu.add_cascade(label = 'Theme', menu = thememenu)
thememenu.add_command(label = 'Monolitik', command=monolitik)
thememenu.add_command(label = 'Light', command=light)

fontmenu = Menu(preferencemenu, tearoff=0)
preferencemenu.add_cascade(label = 'Font', menu = fontmenu)
fontmenu.add_command(label = 'Zoom +', command=zoom_plus)
fontmenu.add_command(label = 'Zoom -', command=zoom_minus)
fontmenu.add_command(label = 'Default', command=default)

# ******************************* SENDING OPTION *******************************

sendmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Send', menu = sendmenu)
sendmenu.add_command(label = 'E-mail', command = send_mail)

# ********************************** STATUS BAR ********************************

status = Label(root, text = 'Line:__ Col:__', bd=2, relief=SUNKEN, anchor = E)
status.pack(side = BOTTOM, fill = X)

root.mainloop()
