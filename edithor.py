
from tkinter import *
import os
from tkinter import filedialog


def  Opener(text):
    try:
            fileName = filedialog.askopenfilename(
                initialdir = os.getcwd(),
                title='Open',filetypes=(('text files','*txt'),('python files','*py',),
                                        ('html file','*.html'),('css file','*.css')))
            print(fileName)
                                    
            with open(fileName , 'r') as f:
                word = f.read()
            text.insert(INSERT,word)
    except TypeError:
            print('NO FILE CHOSEN!')
    except:
        pass

def New(text):
    pass
            
            
def Save(text):
    fileName = filedialog.asksaveasfilename(initialdir=os.getcwd,title='Save',
    filetypes=(('text files','*txt'),('python files','*py',),
                                        ('html file','*.html'),('css file','*.css')))
    with open(fileName,'w') as f:
        f.write(text.get('1.0',END))
        f.close()


def saveAs(text):
    fileName = filedialog.asksaveasfilename(initialdir=os.getcwd(),title='Save As',
        filetypes=(('text files','*txt'),('python files','*py',),
                                        ('html file','*.html'),('css file','*.css')))
    with open(fileName +'\n','a') as f:
        f.write(text.get('1.0',END))  
        f.close() 

        


if __name__ == '__main__':
    Save(text)
    Opener(text)
