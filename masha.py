import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import webbrowser
import sys
import os

filename = ""
fileinput = ""
fontsize = 10




def getinput():
    global fileinput
    fileinput = input_text_area.get("1.0",'end-1c')

def openfile(*e):
    getinput()
    global filename
    global fileinput
    global root

    filename = filedialog.askopenfilename()

    if filename != "":
        file = open(filename,"r")
        fileinput = file.read()
        file.close()
        input_text_area.delete(1.0, "end-1c")
        input_text_area.insert("end-1c", fileinput)
        root.title(filename+" - Masha")
        lent.set(len(input_text_area.get("1.0",tk.END)))
        menu.entryconfig(5, label="Lenght :"+str(lent.get()))

def openfile_(filename2):
    global filename
    global fileinput
    global root
    filename = filename2
    file = open(filename,"r")
    fileinput = file.read()
    file.close()
    input_text_area.delete(1.0, "end-1c")
    input_text_area.insert("end-1c", fileinput)
    root.title(filename+" - Masha")
    lent.set(len(input_text_area.get("1.0",tk.END)))
    menu.entryconfig(5, label="Lenght :"+str(lent.get()))

def savefile(*e):
    getinput()
    global filename
    global fileinput

    if filename != "":
        root.title(filename+" - Masha")
        file = open(filename,"w")
        file.write(fileinput)
        file.close()
    else:
        filename = filedialog.asksaveasfilename(title = "Save")
        if filename != "":
            root.title(filename+" - Masha")
            file = open(filename,"w")
            file.write(fileinput)
            file.close()

def newfile(*e):
    global filename
    filename = filedialog.asksaveasfilename(title = "New")

    if filename != "":
        root.title(filename+" - Masha")
        file = open(filename,"w+")
        fileinput = file.read()
        file.close()
        input_text_area.delete(1.0, "end-1c")
        input_text_area.insert("end-1c", fileinput)

def saveasfile(*e):
    getinput()
    global filename
    global fileinput

    filename = filedialog.asksaveasfilename(title = "Save as")
    if filename != "":
        root.title(filename+" - Masha")
        file = open(filename,"w")
        file.write(fileinput)
        file.close()

def unsaved(event=None):
    root.title(filename+" - Masha *")
    lent.set(len(input_text_area.get("1.0",tk.END)))
    menu.entryconfig(5, label="Lenght :"+str(lent.get()))

def plus(*e):
    global fontsize
    fontsize+=1
    input_text_area.configure(font=("Arial",fontsize))

def minus(*e):
    global fontsize
    if fontsize > 1:
        fontsize-=1
        input_text_area.configure(font=("Arial",fontsize))

def pm(event):
    global fontsize
    if event.delta > 0:
        fontsize+=1
        input_text_area.configure(font=("Arial",fontsize))
    elif event.delta < 0:
        if fontsize > 1:
            fontsize-=1
            input_text_area.configure(font=("Arial",fontsize))

def exitc(*e):
    exit()

def select_all(event=None):
    input_text_area.tag_add('sel', '1.0', 'end')
    return "break"

def copy_lenght(event=None):
    root.clipboard_clear()
    root.clipboard_append(len(fileinput))

def web(event=None):
    webbrowser.open("https://takeb1nzyto.space")

def about(event=None):
    messagebox.showinfo("About", "Masha Text Editor created by OldGameBox.\nThank you for using our software!")

root = tk.Tk()
root.title("Masha")
root.geometry("650x500")
root.minsize(300, 150)



menu = tk.Menu(root)

root.config(menu=menu)

root.bind("<Prior>", plus)
root.bind("<Next>", minus)
root.bind('<Control-s>', savefile)
root.bind('<Control-MouseWheel>', pm)
root.bind('<Control-d>', saveasfile)
root.bind('<Control-o>', openfile)
root.bind('<Control-n>', newfile)
root.bind('<Control-e>', exitc)



input_text_area = tk.Text(root, font=("Arial",10),undo=True,autoseparators=True,maxundo=-1)
input_text_area.pack(expand=True, fill='both')
input_text_area.bind('<<Modified>>', lambda event: unsaved())
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="New", accelerator="Ctrl+N", command=newfile)
file_menu.add_command(label="Open", accelerator="Ctrl+O", command=openfile)
file_menu.add_command(label="Save", accelerator="Ctrl+S", command=savefile)
file_menu.add_command(label="Save as", accelerator="Ctrl+D", command=saveasfile)
file_menu.add_separator()
file_menu.add_command(label="Exit", accelerator="Ctrl+E", command=exitc)

edit_menu = tk.Menu(menu, tearoff=0)
edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=input_text_area.edit_undo)
edit_menu.add_command(label="Redo", accelerator="Ctrl+Shift+Z", command=input_text_area.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: root.focus_get().event_generate('<<Cut>>'))
edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: root.focus_get().event_generate('<<Copy>>'))
edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: root.focus_get().event_generate('<<Paste>>'))
edit_menu.add_separator()
edit_menu.add_command(label='Select All', underline=7, accelerator='Ctrl+A', command=select_all)

about_menu = tk.Menu(menu, tearoff=0)
about_menu.add_command(label="Website", command=web)
about_menu.add_command(label="About", command=about)


menu.add_cascade(label='File', menu=file_menu)
menu.add_cascade(label='Edit', menu=edit_menu)
menu.add_cascade(label='About', menu=about_menu)
menu.add_command(label="|", activebackground=menu.cget("background"))

lent = tk.IntVar(root, 0)
root.bind('<KeyPress>', unsaved)
menu.add_command(label="Lenght :"+str(lent.get()), command=copy_lenght)

if len(sys.argv) != 1:
    if not "python" in sys.argv[0]:
        if len(sys.argv) > 1:
            openfile_(sys.argv[len(sys.argv)-1])
    else:
        if len(sys.argv) > 2:
            openfile_(sys.argv[len(sys.argv) - 1])
root.mainloop()
