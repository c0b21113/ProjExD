
import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker



        



def key_down(event):
    global key
    key=event.keysym

def key_up(event):
    global key
    key=""

def main_proc():
    global cx,cy,mx,my
    if key=="w":
        my-=1
    elif key=="s":
        my+=1
    elif key=="a":
        mx-=1
    elif key=="d":
        mx+=1
    elif key=="Right":
        mx+=1
    elif key=="Left":
        mx-=1
    elif key=="Up":
        my-=1
    elif key=="Down":
        my+=1
    if maze[my][mx]==0:
        cx,cy=mx*100+50,my*100+50
    else:
        if key=="Right":
            maze[my][mx]=0
            mx-=1
        elif key=="Left":
            maze[my][mx]=0
            mx+=1
        elif key=="Up":
            maze[my][mx]=0
            my-=1
        elif key=="Down":
            maze[my][mx]=0
            my+=1
        if key=="w":
            my+=1
        elif key=="s":
            my-=1
        elif key=="a":
            mx+=1
        elif key=="d":
            mx-=1
        

    canv.coords("tori",cx,cy)
    proc=root.after(100,main_proc)




if __name__ == "__main__" :
    root=tk.Tk()
    root.title("迷えるこうかとん")
    canv=tk.Canvas(root,width=1500,height=900,bg="#000000")
    maze=maze_maker.make_maze(15,9)
    maze_maker.show_maze(canv,maze)
    tori=tk.PhotoImage(file="ex03/fig/fig/3.png")
    cx,cy=300,400
    my,mx=1,1
    count_dig=5
    canv.create_image(cx,cy,image=tori, tag="tori")
    canv.pack()

    key=""

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    main_proc()


    root.mainloop()





    
