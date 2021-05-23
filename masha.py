import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font
import webbrowser
import sys, os
import random

filename = ""
fileinput = ""
fontsize = 12
fontt = "Arial"

colors = {
    "voids": "lightgreen",
    "types": "blue",
    "sym": "red",
    "iff": "orange"
}

voids = ["public ", "global ", "static ", "private ", "override ", 'import ']
types = ["int", "float", "string", "char", "bool", "boolean", "double", "long"]
iff = ["if ", "else", "elif ", "for ", "until ", "case ", "witch ", "in"]
sym = ["=", "-", "+", "*", "/", "!", ">", "<", "&", "|", "(", ")", "%",
       "^", "{", "}", ":", "'", '"', "[", "]", ";"]

bg = "#f7e9c1"
fg = "#000000"


# if "python" in sys.argv[0]:
#     os.system("pip install notify-py")
# if sys.platform == "linux":
#     print('Please install libnotify for normal work: "sudo apt install libnotify"')

# print(os.path.dirname(__file__))


# os.chdir(os.path.dirname(__file__))

# from notifypy import Notify


# def send_not(title, message):
#     notification = Notify()
#     notification.title = title
#     notification.message = message
#     notification.icon = "masha.png"
#
#     notification.send()

def getinput():
    global fileinput
    fileinput = input_text_area.get("1.0", 'end-1c')



def openfile(*e):
    getinput()
    global filename
    global fileinput
    global root

    filename = filedialog.askopenfilename()

    if filename != "":
        file = open(filename, "r")
        fileinput = file.read()
        file.close()
        input_text_area.delete(1.0, "end-1c")
        input_text_area.insert("end-1c", fileinput)
        root.title(filename + " - Masha")
        lent.set(len(input_text_area.get("1.0", tk.END)))
        menu.entryconfig(8, label="Lenght :" + str(lent.get()))
        analiz()


def openfile_(filename2):
    global filename
    global fileinput
    global root
    filename = filename2
    file = open(filename, "r")
    fileinput = file.read()
    file.close()
    input_text_area.delete(1.0, "end-1c")
    input_text_area.insert("end-1c", fileinput)
    root.title(filename + " - Masha")
    lent.set(len(input_text_area.get("1.0", tk.END)))
    menu.entryconfig(8, label="Lenght :" + str(lent.get()))
    analiz()


def savefile(*e):
    getinput()
    global filename
    global fileinput

    if filename != "":
        root.title(filename + " - Masha")
        file = open(filename, "w")
        file.write(fileinput)
        file.close()
        # send_not("Masha", "File Saved!")
    else:
        filename = filedialog.asksaveasfilename(title="Save")
        if filename != "":
            root.title(filename + " - Masha")
            file = open(filename, "w")
            file.write(fileinput)
            file.close()
            # send_not("Masha", "File Saved!")


def newfile(*e):
    global filename
    filename = filedialog.asksaveasfilename(title="New")

    if filename != "":
        root.title(filename + " - Masha")
        file = open(filename, "w+")
        fileinput = file.read()
        file.close()
        input_text_area.delete(1.0, "end-1c")
        input_text_area.insert("end-1c", fileinput)


def saveasfile(*e):
    getinput()
    global filename
    global fileinput

    filename = filedialog.asksaveasfilename(title="Save as")
    if filename != "":
        root.title(filename + " - Masha")
        file = open(filename, "w")
        file.write(fileinput)
        file.close()


def unsaved(event=None):
    global fileinput
    if fileinput != input_text_area.get("1.0", 'end-1c'):
        root.title(filename + " - Masha *")
        lent.set(len(input_text_area.get("1.0", tk.END)))
        menu.entryconfig(8, label="Lenght :" + str(lent.get()))
        analiz()
    else:
        root.title(filename + " - Masha")


def analiz():
    input_text_area.tag_delete("iff")
    for element in range(len(iff)):
        highlight(iff[element], "iff")
    input_text_area.tag_delete("sym")
    for element in range(len(sym)):
        highlight(sym[element], "sym")
    input_text_area.tag_delete("voids")
    for element in range(len(voids)):
        highlight(voids[element], "voids")
    input_text_area.tag_delete("types")
    for element in range(len(types)):
        highlight(types[element], "types")

def plus(*e):
    global fontsize
    fontsize += 1
    input_text_area.configure(font=(fontt, fontsize))


def minus(*e):
    global fontsize
    if fontsize > 1:
        fontsize -= 1
        input_text_area.configure(font=(fontt, fontsize))


def pm(event):
    global fontsize
    if event.delta > 0:
        fontsize += 1
        input_text_area.configure(font=(fontt, fontsize))
    elif event.delta < 0:
        if fontsize > 1:
            fontsize -= 1
            input_text_area.configure(font=(fontt, fontsize))


def exitc(*e):
    exit()


def select_all(event=None):
    input_text_area.tag_add('sel', '1.0', 'end')
    return "break"


def copy_lenght(event=None):
    root.clipboard_clear()
    root.clipboard_append(lent.get())


def web(event=None):
    webbrowser.open("https://github.com/OldGameBox/Masha-text-editor")


def about(event=None):
    messagebox.showinfo("About", "Masha Text Editor created by OldGameBox.\nThank you for using our software!")


def tab(arg):
    input_text_area.insert(tk.INSERT, " " * 4)
    return 'break'


def maria(event=None):
    global fontt
    fontt = random.choice(fonts)
    menu.entryconfig(1, font=(fontt, 12))
    menu.entryconfig(2, font=(fontt, 12))
    menu.entryconfig(3, font=(fontt, 12))
    menu.entryconfig(4, font=(fontt, 12))
    menu.entryconfig(5, font=(fontt, 12))
    menu.entryconfig(6, font=(fontt, 12))
    menu.entryconfig(7, font=(fontt, 12))
    menu.entryconfig(8, font=(fontt, 12))
    input_text_area.configure(font=(fontt, fontsize))


def tabs(event=None):
    line_text = input_text_area.get("insert linestart", "insert lineend")
    spaces = 0
    for letter in line_text:
        if letter == " ":
            spaces += 1
        else:
            break
    spaces = spaces // 4
    try:
        if line_text[-1] == ":" or line_text[-1] == "{":
            spaces += 1
        elif line_text[-2] == ":" and line_text[-1] == " " or line_text[-2] == "{" and line_text[-1] == " ":
            spaces += 1
    except:
        spaces = spaces
    text = "\n" + "    " * spaces
    input_text_area.insert("insert", text)
    return 'break'


def back(event=None):
    if input_text_area.get("insert-4c", "insert") == "    ":
        input_text_area.delete("insert-4c", "insert")
        return 'break'


def change_theme(event=None):
    if dark.get():
        input_text_area.configure(bg=fg, fg=bg)
        menu.configure(bg=fg, fg=bg)
        scrollbar.configure(bg=fg)
        scrollbar2.configure(bg=fg)
        menu.entryconfig(1, activebackground=menu.cget("background"))
        menu.entryconfig(2, activebackground=menu.cget("background"))
        menu.entryconfig(7, activebackground=menu.cget("background"))
        input_text_area.configure(insertbackground=bg)
    else:
        input_text_area.configure(bg=bg, fg=fg)
        menu.configure(bg=bg, fg=fg)
        scrollbar.configure(bg=bg)
        scrollbar2.configure(bg=bg)
        menu.entryconfig(1, activebackground=menu.cget("background"))
        menu.entryconfig(2, activebackground=menu.cget("background"))
        menu.entryconfig(7, activebackground=menu.cget("background"))
        input_text_area.configure(insertbackground=fg)


def highlight(seq, highlight):
    global input_text_area
    i = len(seq)
    index = "1.0"

    while True:
        index = input_text_area.search(seq, index, nocase=1, stopindex='end', exact=False)
        if not index: break
        index2 = "%s+%dc" % (index, i)
        input_text_area.tag_add(highlight, index, index2)
        input_text_area.tag_config(highlight, foreground=colors[highlight])
        index = index2



root = tk.Tk()
root.title("Masha")
root.geometry("650x500")
root.minsize(300, 150)
root.iconphoto(False, tk.PhotoImage(file='masha.png'))

fonts = font.families()

menu = tk.Menu(root)

root.config(menu=menu)

root.bind("<Control-Key-1>", plus)
root.bind("<Control-Key-2>", minus)
root.bind('<Control-s>', savefile)
root.bind('<Control-MouseWheel>', pm)
root.bind('<Control-d>', saveasfile)
root.bind('<Control-o>', openfile)
root.bind('<Control-n>', newfile)
root.bind('<Control-e>', exitc)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar2 = tk.Scrollbar(root, orient="horizontal")
scrollbar2.pack(side=tk.BOTTOM, fill=tk.X)

input_text_area = tk.Text(root, font=("Arial", fontsize), undo=True, autoseparators=True, maxundo=-1,
                          yscrollcommand=scrollbar.set,
                          xscrollcommand=scrollbar2.set,
                          wrap="none")
input_text_area.configure(insertbackground=fg)
scrollbar.config(command=input_text_area.yview)
scrollbar2.config(command=input_text_area.xview)
input_text_area.pack(expand=True, fill='both')
input_text_area.bind('<<Modified>>', lambda event: unsaved())
input_text_area.bind("<Tab>", tab)
input_text_area.bind("<Return>", tabs)
input_text_area.bind("<BackSpace>", back)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

menu.add_command(label="Masha", font='Arial 12 bold', activebackground=menu.cget("background"))

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

theme_menu = tk.Menu(menu, tearoff=0)

theme_menu.add_command(label="Zoom in", command=plus)
theme_menu.add_command(label="Zoom out", command=minus)
theme_menu.add_separator()
theme_menu.add_command(label="Font", command=maria)
dark = tk.IntVar(root, 1)
change_theme()
theme_menu.add_checkbutton(label="DarkMode", onvalue=1, offvalue=0, variable=dark, command=change_theme)

about_menu = tk.Menu(menu, tearoff=0)
about_menu.add_command(label="Website", command=web)
about_menu.add_command(label="About", command=about)

menu.add_command(label="|", activebackground=menu.cget("background"))
menu.add_cascade(label='File', menu=file_menu)
menu.add_cascade(label='Edit', menu=edit_menu)
menu.add_cascade(label='Appearance', menu=theme_menu)
menu.add_cascade(label='About', menu=about_menu)
menu.add_command(label="|", activebackground=menu.cget("background"))

lent = tk.IntVar(root, 0)
root.bind('<KeyPress>', unsaved)
menu.add_command(label="Lenght :" + str(lent.get()), command=copy_lenght)

if len(sys.argv) != 1:
    if not "python" in sys.argv[0]:
        if len(sys.argv) > 1:
            openfile_(sys.argv[len(sys.argv) - 1])
    else:
        if len(sys.argv) > 2:
            openfile_(sys.argv[len(sys.argv) - 1])

root.mainloop()
