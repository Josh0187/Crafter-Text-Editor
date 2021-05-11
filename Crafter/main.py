import tkinter.filedialog
from tkinter import *
from tkinter import Toplevel, Button, Tk, Menu
import os
import time
import tkinter.font as tkFont


root = Tk()
root.title('Crafter')
root.geometry("800x600")
icon_image = PhotoImage(file = "C:/Users/parsa/OneDrive/Desktop/Crafter/icons/crafter.png")
root.iconphoto(False, icon_image)
main_frame = Frame(root)
formating_bar_frame = Frame(root)

# Default Font
customFont = tkFont.Font(family = "Helvetica", size = 12)
text=Text(main_frame, font = customFont)

# Global Variables
checkBold = 0
checkItalic = 0
checkUnderline = 0
current_path = ""
openfile_flag = 0

# Formating bar
# Font selection
font = Menubutton(formating_bar_frame, text = "Font | Select*", width = 15)

def FontHelvetica():
    font.config(text = "Font | Helvetica")
    customFont.configure(family = "Helvetica")

def FontCourier():
    font.config(text = "Front | Courier")
    customFont.configure(family = "Courier")

font.pack(side = LEFT)
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu

Helvetica = IntVar()
arial = IntVar()
times = IntVar()
Courier = IntVar()

font.menu.add_checkbutton(label = "Courier",font = "Courier", variable = Courier, command = FontCourier)
font.menu.add_checkbutton(label = "Helvetica", font = "Helvetica", variable = Helvetica, command = FontHelvetica)

# Spacing selection
spacing = Menubutton(formating_bar_frame, text = "Spacing | *", width = 10) 

def space0():
    spacing.config(text = "Spacing | 0")
    text.config(spacing1 = 0)

def space1():
    spacing.config(text = "Spacing | 1")
    text.config(spacing1 = 10)

def space2():
    spacing.config(text = "Spacing | 2")
    text.config(spacing1 = 20)

spacing.pack(side = LEFT)
spacing.menu = Menu(spacing, tearoff=0)
spacing["menu"] = spacing.menu

spacing0 = IntVar()
spacing1 = IntVar()
spacing2 = IntVar()

spacing.menu.add_checkbutton(label = "0",variable = spacing0, command = space0)
spacing.menu.add_checkbutton(label = "1",variable = spacing1, command = space1)
spacing.menu.add_checkbutton(label = "2",variable = spacing2, command = space2)

# Font Sizing
font_size_label = Label(formating_bar_frame, text = "Font Size | *", width = 10)
font_size_label.pack(side = LEFT)
font_size_spin = Spinbox(formating_bar_frame, from_=0, to = 60, width = 10)
font_size_spin.pack(side = LEFT)

def changeFontSize(event=None):
    fontSize = font_size_spin.get()
    customFont.configure(size = fontSize)

root.bind('<Return>', changeFontSize)
font_size_button = Button(formating_bar_frame, text= "Enter", width = 5, command = changeFontSize)
font_size_button.pack(side = LEFT, padx = 5)

# Bolding
def bold(event=None):
    global checkBold
    if checkBold == 0:
        customFont.configure(weight = "bold")
        checkBold = 1
    else: 
        customFont.configure(weight = "normal")
        checkBold = 0

bold_image = PhotoImage(file = "C:/Users/parsa/OneDrive/Desktop/Crafter/icons/bold.png")
bold_button = Button(formating_bar_frame, text = "Bold", width = 20 , image = bold_image, command = bold)
bold_button.pack(side = LEFT)
root.bind('<Control-b>', bold)

# Italics
def italic(event=None):
    global checkItalic
    if checkItalic == 0:
        customFont.configure(slant = "italic")
        checkItalic = 1
    else: 
        customFont.configure(slant = "roman")
        checkItalic = 0

italics_image = PhotoImage(file = "C:/Users/parsa/OneDrive/Desktop/Crafter/icons/italics.png")
italic_button = Button(formating_bar_frame, text = "italic", width = 20, image = italics_image, command = italic)
italic_button.pack(side = LEFT)
root.bind('<Control-i>', italic)

# underline
def underline(event=None):
    global checkUnderline
    if checkUnderline == 0:
        customFont.configure(underline = 1)
        checkUnderline = 1
    else: 
        customFont.configure(underline = 0)
        checkUnderline = 0

underline_image = PhotoImage(file = "C:/Users/parsa/OneDrive/Desktop/Crafter/icons/underline.png")
underline_button = Button(formating_bar_frame, text = "Underline", width = 20,image = underline_image, command = underline)
underline_button.pack(side = LEFT)
root.bind('<Control-u>', underline)


# Displaying Main Text and formating bar
text.pack(side = "top", expand=True, fill='both')
text.grid_columnconfigure(0, weight=1)
text.grid_rowconfigure(0, weight = 1)
formating_bar_frame.pack(side = "top", fill = 'both')
main_frame.pack(side = "top", expand=True, fill = 'both')

# def save():
#    if opened_or_new == 1:
#        saveas()
#    else:
#        t = text.get("1.0", "end-1c")
#        file3 = open(opened_path, "w+")
#        file3.write(t)
#        file3.close()

# Menu functions
# Save As
def saveas():
    t = text.get("1.0", "end-1c")
    savelocation=tkinter.filedialog.asksaveasfilename(title = "Select file")
    global current_path
    current_path = savelocation
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()

# Save
def save():
    if current_path != "":
        t = text.get("1.0", "end-1c")
        file2 = open(current_path, "w+")
        file2.write(t)
        file2.close()
    
    else:
        saveas()

# Slightly broken: cannot format text using formating bar after called
# fix: i think to fix it you have to modify text not make a new Text called opentext
def openfile():
        global openfile_flag
        global current_path
        print(openfile_flag)
        if len(text.get("1.0", "end-1c")) == 0 or openfile_flag == 1:
            openfile_flag = 0
            openlocation = tkinter.filedialog.askopenfilename(title = "Select file")
            current_path = openlocation
            file2 = open(openlocation, "r")
            text.delete('1.0', END)
            for line in file2:
                text.insert(END,line)
            file2.close()
            return
        
        def yes():
            global openfile_flag
            if current_path != "":
                save()
                ask.destroy()
                print("setting openfile_flag to 1")
                openfile_flag = 1
                openfile()
            else:
                saveas()
                text.delete('1.0', END)
                ask.destroy()
                openfile()
                
        
        def no():
            text.delete('1.0', END)
            ask.destroy()
            openfile()

        ask = Frame(root)
        ask_label = Label(ask, text = "Would you like to save your progress?", font=('Helvetica', 18, 'bold'))
        ask_label.pack()
        yes_button = Button(ask, text = "Yes", command = yes)
        yes_button.pack()
        no_button = Button(ask, text = "No", command = no)
        no_button.pack()
        ask.pack()        
        

        
# 
def new():
    if len(text.get("1.0", "end-1c")) == 0:
        return
    else:
        def yes():
            saveas()
            text.delete('1.0', END)
            ask.destroy()

        def no():
            text.delete('1.0', END)
            ask.destroy()

        ask = Frame(root)
        ask_label = Label(ask, text = "Would you like to save your progress?", font=('Helvetica', 18, 'bold'))
        ask_label.pack()
        yes_button = Button(ask, text = "Yes", command = yes)
        yes_button.pack()
        no_button = Button(ask, text = "No", command = no)
        no_button.pack()
        ask.pack()

    

def close():
    file.destroy()

# Creating Top menu bar
menubar = Menu(root)
file = Menu(menubar, tearoff = 0)
file.add_command(label = "New", command = new)
file.add_command(label = "Open", command = openfile)
file.add_command(label = "Save", command = save)
file.add_command(label = "Save as", command = saveas)
file.add_command(label = "Close", command = close)

file.add_separator()
file.add_command(label = "Exit", command = root.quit)
menubar.add_cascade(label="File", menu=file)  
menubar.config(font = "Helvetica 10 bold italic")

root.config(menu = menubar)
root.mainloop()