import pyautogui
from tkinter import  *
def takess():
    a = entry.get()
    path = a +"\\image.png"
    print(path)
    ss = pyautogui.screenshot()
    ss.save(path)
window = Tk()
window.title("desktop screenshot application project")
window.geometry("300x300")
window.config(bg="beige")
window.resizable(False,False)
entry = Entry(window,font=("Time New Roman",10))
entry.place(x=20,y=50, height=50,width=400)
btn =  Button(window,text="Shot",font=("Time New Roman",25),command=takess)
btn.place(x=100,y=100,height=50,width=100)
window.mainloop()
