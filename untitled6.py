from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
root=Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.configure(bg="RoyalBlue2")
open_image = ImageTk.PhotoImage(Image.open ("open.png"))
save_image = ImageTk.PhotoImage(Image.open ("save.png"))
exit_image = ImageTk.PhotoImage(Image.open ("exit.jpg"))
label_file_name = Label(root, text="File Name : ")
label_file_name.place(relx=0.28,rely=0.03,anchor=CENTER)
input_file_name = Entry(root, bg="lightblue1")
input_file_name.place(relx=0.46,rely=0.03,anchor=CENTER)
my_text = Text(root,height=35,width=80, bg="lightblue1")
my_text.place(relx=0.5,rely=0.55, anchor=CENTER)

name = ""
def openfile():
    global name
    my_text.delete(1.0, END)
    input_file_name.delete(0, END)
    html_file = filedialog.askopenfilename(title = " Open HTML File", filetypes=(("HTML Files", "*.html"),))
    print(html_file)
    name=os.path.basename(html_file)
    formated_name = name.split('.')[0]
    html_file = open(name,'r')
    paragraph = html_file.read()
    my_text.insert(END,paragraph)
    html_file.close()
    
open_button = Button(root,image=open_image,command=openfile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
root.mainloop()