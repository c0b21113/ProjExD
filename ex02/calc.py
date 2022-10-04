import tkinter as tk
import tkinter.messagebox as tkm
import math

root=tk.Tk()
root.geometry("400x700")
R=2#数字ボタンのrowの開始行目
C=0
R2=1#四則演算のボタンのrowの開始行目

def button_click(event):
    btn=event.widget
    txt=btn["text"]
    #tkm.showinfo(txt,f"[{txt}ボタンが押されました]")
    entry.insert(tk.END,txt)

def button_click2(event):
    btn2=event.widget
    txt=btn2["text"]
    entry.insert(tk.END,txt)

def req_click(event):
    ans=eval(entry.get())
    entry.delete(0,tk.END)
    entry.insert(tk.END,ans)

def AC_click(event):
    entry.delete(0,tk.END)

def button_buf(event):
    event.widget["bg"]="#CCFFFF"#水色
    

def button_buf2(event):
    event.widget["bg"]="#C0C0C0"#灰色

def leave_button_buf(event):
    event.widget["bg"]='Yellow1' #色を元に戻す

def leave_button_buf2(event):
    event.widget["bg"]='SystemButtonFace' #色を元に戻す

def change(event):
    event.widget
    entry.insert(0,"-") #-の数字に符号変更

def make_sqrt(event):
    figure=int(entry.get())
    ans=math.sqrt(figure)
    entry.delete(0,tk.END)
    entry.insert(tk.END,ans) #平方根をinsertする

def make_e(event):
    num=int(entry.get())
    ans=math.exp(num)
    entry.delete(0,tk.END)
    entry.insert(tk.END,ans) #e^nをinsertする


entry=tk.Entry(root,justify="right",width=10,font=("Times New Roman",40))
entry.grid(row=0,column=0,columnspan=3)#入力された数字を映す欄の生成


for j in ["+","-","*","/","**"]:
    button2=tk.Button(root,text=j,width=4,height=2,font=("Times New Roman",30),bg="yellow1")
    button2.bind("<1>",button_click2)
    button2.bind("<Enter>",button_buf)
    button2.bind("<Leave>",leave_button_buf)
    button2.grid(row=R2,column=4)
    R2+=1 #ここで足して下に連ねる

#以下、botton〇は数字と四則演算のボタン以外のボタンを生成し、bindでマウスオーバー、クリックの際の挙動を決定している

button3=tk.Button(root,text="=",width=4,height=2,font=("Times New Roman",30))
button3.bind("<1>",req_click)
button3.bind("<Enter>",button_buf2)
button3.bind("<Leave>",leave_button_buf2)
button3.grid(row=5,column=1)


button4=tk.Button(root,text="AC",width=4,height=2,font=("Times New Roman",30))
button4.bind("<1>",AC_click)
button4.bind("<Enter>",button_buf2)
button4.bind("<Leave>",leave_button_buf2)
button4.grid(row=5,column=2)


button5=tk.Button(root,text="+/-",width=4,height=2,font=("Times New Roman",30),bg="yellow1")
button5.bind("<1>",change)
button5.bind("<Enter>",button_buf)
button5.bind("<Leave>",leave_button_buf)
button5.grid(row=1,column=0)


button6=tk.Button(root,text="√",width=4,height=2,font=("Times New Roman",30),bg="yellow1")
button6.bind("<1>",make_sqrt)
button6.bind("<Enter>",button_buf)
button6.bind("<Leave>",leave_button_buf)
button6.grid(row=1,column=1)


button7=tk.Button(root,text="e^n",width=4,height=2,font=("Times New Roman",30),bg="yellow1")
button7.bind("<1>",make_e)
button7.bind("<Enter>",button_buf)
button7.bind("<Leave>",leave_button_buf)
button7.grid(row=1,column=2)


#数字のボタンをrangeで生成している

for i in range(9,-1,-1):
    button=tk.Button(root,text=f"{i}",width=4,height=2,font=("Times New Roman",30))
    button.bind("<1>",button_click)
    button.bind("<Enter>",button_buf2)
    button.bind("<Leave>",leave_button_buf2)
    button.grid(row=R,column=C)
    if C==2:
        R+=1#改行
        C=0
    else:
        C+=1#横に並べる

root.mainloop()