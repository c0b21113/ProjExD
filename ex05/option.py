import tkinter as tk
from tkinter import messagebox as tkm

from ex05.fight_kokaton import perfect_body, turth,ans


def button_click(event):
    btn=event.widget
    txt=btn["text"]
    if turth==ans:
        perfect_body+=1#無敵回数を追加
        success_point+=1
    else:
        return 