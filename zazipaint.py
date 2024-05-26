import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox

canvas_w = 800
canvas_h = 600

global opened_name
opened_name = False

def paint( event ):
    py_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x +1), (event.y + 1)
    w.create_oval(x1, y1, x2, y2, fill=py_green)
Master= Tk()
Master.title("ZaziPaint")
w = Canvas(Master,
    width=canvas_w,
    height=canvas_h)
w.pack(expand =YES, fill=BOTH)
w.bind( "<B1-Motion>", paint)

#create new file
def new_file():
    w.delete("1.0", END)
    Master.title("New File")
    global opened_name
    opened_name = False

#open file
def open_file():
    w.delete("1.0", END)
    t_file = filedialog.askopenfilename(initialdir="@/home", title="Open File", filetypes=(("PNG Files", "*.png"),("All Files", "*.*")))
    if t_file:
        global opened_name
        opened_name = t_file
        name = t_file
        t_file = open(t_file, 'r')
        stuff = t_file.read()
        w.insert(END, stuff)
        t_file.close()
#save as file
def save_as_file(e=False):
    global opened_name
    t_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="@/home", title="Save File", filetypes=(("PNG Files", "*.png"),("All Files", "*.*")))
    opened_name = t_file
    t_file = open(t_file, 'w')
    t_file.write(w.get(1.0, END))
    t_file.close()


#save file
def save_file(e=False):
    global opened_name
    if opened_name:
        t_file = open(opened_name, 'w')
        t_file.write(w.get(1.0, END))
        m_box = messagebox.showinfo("Saved", "File saved successfully") 
        t_file.close()
    else:
        save_as_file()

def cut_text(e=False):
    global selected
    if e:
        selected = Master.clipboard_get()
    else:
        if w.selection_get():
            selected = w.selection_get()
            w.delete("sel.first", "sel.last")
            Master.clipboard_clear()
            Master.clipboard_append(selected)

def save_file(e=False):
    global opened_name
    if opened_name:
        t_file = open(opened_name, 'w')
        t_file.write(w.get(1.0, END))
        m_box = messagebox.showinfo("Saved", "File saved successfully") 
        t_file.close()
    else:
        save_as_file()

#menu
m_menu = Menu(Master)
Master.config(menu=m_menu)

#file menu
f_menu = Menu(m_menu, tearoff=False)
m_menu.add_cascade(label="File", menu=f_menu)
f_menu.add_command(label="New", command=new_file)
f_menu.add_command(label="Open", command=open_file)
f_menu.add_command(label="Save", command=save_file)
f_menu.add_command(label="Save as", command=save_as_file)
f_menu.add_separator()
f_menu.add_command(label="Exit", command=Master.quit)

#edit menu
e_menu = Menu(m_menu, tearoff=False)
m_menu.add_cascade(label="Edit", menu=e_menu)

#edit bindings
Master.bind('<Control-Key-s>', save_file)
Master.bind('<Control-Key-S>', save_as_file)

w.update()
w.postscript(file="file_name.ps", colormode='color')

mainloop()
