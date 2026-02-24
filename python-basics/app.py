#Maureen Mbugua
#19/02/2026


from tkinter import *
def hello():
    print("hello from Reenie")
root = Tk()
root.geometry("600x600")

frame_one = Frame(root)
frame_one.pack()

button_one = Button(frame_one,text="say hello",command= hello)
button_one.pack

root.mainloop()

