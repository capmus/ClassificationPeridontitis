import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
#import tensorflow.image as tf_image
import os
import cv2
import tensorflow as tf
import numpy as np
#load the trained model to classify sign
from keras.models import load_model
model = load_model(os.path.join('ClassificationPeriodontitis25epd1.h5'))

classes = {
    0: 'Prediction Class is NON Periodontitis',
    1: 'Prediction Class is Periodontitis'
}

#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Periodontitis classification')
top.configure(background='#CDCDCD')

label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    #global label_packed
    img = cv2.imread(file_path)
    imgC = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    resize = tf.image.resize(imgC, (350,350))
    yhat = model.predict(np.expand_dims(resize/255,0))
    if yhat > 0.5:
        sign = classes[1]
    else:
        sign = classes[0]
    label.configure(foreground='#011638', text=sign) 
   

def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Image",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Know if You have Periodontitis",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()