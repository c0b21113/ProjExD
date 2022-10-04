import tkinter as tk


root=tk.Tk()
root.geometry("300x500")
R=0
C=0
count=0

for i in range(9,-1,-1):
    button=tk.Button(root,text=f"{i}",width=4,height=2,font=("Times New Roman",30))
    button.grid(row=R,column=C)
    count+=1
    if C==2:
        R+=1
        C=0
    else:
        C+=1


root.mainloop()