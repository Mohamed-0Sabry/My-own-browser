from tkinter import *
import webbrowser
root=Tk()
root.title("MNS2")
def search():
    url=entry.get()
    webbrowser.open(url)
label=Label(root ,text="Enter URL Here :    " ,font=("arial" ,15 ,"bold"))
label.grid(row=0 ,column=0)
entry=Entry(root ,width=35)
entry.grid(row=0 ,column=1)
btn=Button(root ,text="Search" ,command=search ,bg="blue" ,fg="white" ,font=("arial" ,14 ,"bold"))
btn.grid(row=1 ,column=0 ,columnspan=10 ,pady=10)

root.mainloop()
