import base64
import io
from io import BytesIO
import re
from tensorflow import keras
import os
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
#from PIL import Image, ImageTk
import tkinter.font as tkFont
from tkinter import ttk

classes = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']

def names(number):
    if(number == 0):
        return 'a Glioma tumor'
    elif(number == 1):
        return 'a Meningioma tumor'
    elif(number == 2):
        return 'no tumor'
    elif(number == 3):
        return 'a Pituitary tumor'

def Detection(fileName):

    img_path = fileName
    img_pil = Image.open(img_path)
    model = load_model(r'/home/pi/model_final.h5')
    dim = (150, 150)

    img = np.array(img_pil.resize(dim))

    x = img.reshape(1,150,150,3)
    answ = model.predict(x)
    classification = np.where(answ == np.amax(answ))[1][0]
    pred=str(round(answ[0][classification]*100 ,3)) + '% confidence there is ' + names(classification)

    print(classification)
        #Second prediction and facts about tumor if there is
    if classification==0:

        facts = '• Glioma is a type of tumor that occurs in the\n brain and spinal cord.A glioma can affect your\n brain function and be life-threatening\n depending on its location and\n rate of growth.'
        no_tumor = str(round(answ[0][2]*100 ,3))
        pred2 = no_tumor + '% confidence there is no tumor'
        strcon = "• "+pred+"\n"+facts+"\n• "+pred2
        print(strcon)
        return(strcon)

    elif classification==1:
        facts = '• A meningioma is a tumor that arises from the meninges,\n the membranes that surround your brain. Most meningiomas\n grow very slowly,often over many years without\n causing symptoms.'
        no_tumor = str(round(answ[0][2]*100 ,3))
        pred2 = no_tumor + '% confidence there is no tumor'
        strcon = "• "+pred+"\n"+facts+"\n• "+pred2
        print(strcon)
        return(strcon)

    elif classification==2:
        facts = 'No Tumor'
        print(facts)
        return(strcon)


    elif classification==3:
        facts = '• Pituitary tumors are abnormal growths\n that develop in your pituitary gland.\n Most pituitary tumors are noncancerous\n (benign) growths that remain in your \n pituitary gland or surrounding tissues.'
        no_tumor = str(round(answ[0][2]*100 ,3))
        pred2 = no_tumor + '% confidence there is no tumor'
        strcon = "• "+pred+"\n"+facts+"\n• "+pred2
        print(strcon)
        return(strcon)

    else:
        facts=None
        pred2 = None





my_w = tk.Tk()
my_w.geometry("450x420")  # Size of the window
my_w.title('Brain Tumor Detection System')
my_font1=('times', 10, 'bold')
GLabel_779=tk.Label(my_w)
ft = tkFont.Font(family='Times',size=10)
GLabel_779["font"] = ft
GLabel_779["fg"] = "#009688"
GLabel_779["justify"] = "center"
GLabel_779["text"] = "Welcome to Brain Tumor Detection System"
GLabel_779["relief"] = "raised"
GLabel_779.grid(row=1,column=0,ipadx=10, ipady=10, padx=10, pady=10)


l1 = tk.Label(my_w,text='Please Choose Photo',width=63,font=my_font1)
l1.grid(row=6,column=0 )
b1 = tk.Button(my_w, text='Upload File',
width=10,command = lambda:upload_file())
b1.grid(row=8,column=0, padx=2, pady=2)
GMessage_206=tk.Label(my_w)


def upload_file():

    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    print(filename)
    stringVal=Detection(filename)
    img=Image.open(filename)
    img_resized=img.resize((200,130)) # new width & height
    img=ImageTk.PhotoImage(img_resized)
    b2 =tk.Button(my_w,image=img) # using Button
    b2.grid(row=10,column=0,ipadx=5, ipady=2, padx=2, pady=2)
    GMessage_206["bg"] = "#f5dede"
    ft = tkFont.Font(family='Times',size=12)
    GMessage_206["font"] = ft
    GMessage_206["fg"] = "#cc0000"
    GMessage_206["justify"] = "left"
    GMessage_206["text"] = stringVal
    GMessage_206.grid(row=12,column=0,ipadx=2, ipady=2, padx=2, pady=2)

my_w.mainloop()  # Keep the window open
