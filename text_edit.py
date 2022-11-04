try:
    from edithor import Opener,Save,saveAs,New
except :
    print('Import Error!')

from pydoc import text
from tkinter import filedialog
from tkinter import *
import os

root =  Tk()
root.geometry('500x500')
root.title('Text Editor')
root.resizable(0,0)

#commands

def openFile(opened):

    if fileVar.get() == 'File':
        pass
    
    if fileVar.get() == 'Open':
        try:
            Opener(txt)
        except:
            pass

        
    if fileVar.get() == 'New':
        try:
            New(txt)
        except:
            pass


    if fileVar.get() == 'Save':
        try:
            Save(txt)
        except:
            pass


    if fileVar.get() == 'Save As':       
        try:
            saveAs(txt)
        except:
            pass
        

#defining frames
frame1 = Frame(root,bg='white')
frame1.pack(fill='x')

frame2 = Frame(root,bg='blue')
frame2.pack()

global fileVar
#option menus

fileOpt = ['File','Open', 'New','Save','Save As']
fileVar = StringVar()
file = OptionMenu(frame1,fileVar,*fileOpt,command=openFile)
file['highlightthickness'] = 0
file['borderwidth'] = 0
fileVar.set(fileOpt[0])
file.grid(row=0,column=0)


editOpt = ['Edit','Select', 'Copy','Paste','Font','Datetime']
editVar = StringVar()
edit = OptionMenu(frame1,editVar,*editOpt)
edit['highlightthickness'] = 0
edit['borderwidth'] = 0
editVar.set(editOpt[0])
edit.grid(row=0,column=1)

formatOpt = ['Format','Wordmap', 'Font']
formatVar = StringVar()
format = OptionMenu(frame1,formatVar,*formatOpt)
format['highlightthickness'] = 0
format['borderwidth'] = 0
formatVar.set(formatOpt[0])
format.grid(row=0,column=2)

veiwOpt = ['Veiw','Status bar', 'Zoom']
veiwVar = StringVar()
veiw = OptionMenu(frame1,veiwVar,*veiwOpt)
veiw['highlightthickness'] = 0
veiw['borderwidth'] = 0
veiwVar.set(veiwOpt[0])
veiw.grid(row=0,column=3)

helpOpt = ['Help','Report', 'Update']
helpVar = StringVar()
help = OptionMenu(frame1,helpVar,*helpOpt)
help['highlightthickness'] = 0
help['borderwidth'] = 0
helpVar.set(helpOpt[0])
help.grid(row=0,column=4)


#btn = Button(frame1,text='click',command=openFile)
#btn.grid(row=0,column=5)

txt = Text(frame2)
txt.pack()


root.mainloop()