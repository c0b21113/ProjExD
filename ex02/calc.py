import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn=event.widget
    txt=btn["text"]
    #tkm.showinfo(txt,f"[{txt}ボタンが押されました]")
    entry.insert(tk.END,txt)

def button_click2(event):
    btn2=event.widget
    txt=btn2["text"]
    entry.insert(tk.END,txt)

def equ_click(event):
    ans=eval(entry.get())
    entry.delete(0,tk.END)
    entry.insert(tk.END,ans)








root=tk.Tk()
root.geometry("500x1000")
R=1
C=0
count=0

entry=tk.Entry(root,justify="right",width=10,font=("Times New Roman",40))
entry.grid(row=0,column=0,columnspan=3)

button2=tk.Button(root,text="+",width=4,height=2,font=("Times New Roman",30))
button2.bind("<1>",button_click2)
button2.grid(row=4,column=1)

button3=tk.Button(root,text="=",width=4,height=2,font=("Times New Roman",30))
button3.bind("<1>",equ_click)
button3.grid(row=4,column=2)

for i in range(9,-1,-1):
    button=tk.Button(root,text=f"{i}",width=4,height=2,font=("Times New Roman",30))
    button.bind("<1>",button_click)
    button.grid(row=R,column=C)
    count+=1
    if C==2:
        R+=1
        C=0
    else:
        C+=1



root.mainloop()