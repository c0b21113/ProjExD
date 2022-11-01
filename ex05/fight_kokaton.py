

import pygame as pg
import sys
from random import randint
import time
import tkinter as tk
from tkinter import messagebox as tkm

from ex05.option import button_click


global success_point

class Screen:
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title) #逃げろ！こうかとん
        self.sfc = pg.display.set_mode(wh) #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) #"fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()
        
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
    pg.K_LEFT:  [-1, 0],
    pg.K_RIGHT: [+1, 0],
    }


class Bird:

    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 900, 400

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


class setsuccess:
    def __init__(self,success_point):
        self.success_point=success_point


class text:#Tキーを押した際に制限時間20秒で問題が表示され、答えると残機が増える
    def __init__(self,question,geo,figure,endtime):
        self.question=question#問題
        self.geo=geo
        self.figure=figure#問題数
        self.endtime=endtime
        question2=question.keys()#問題文と答えを抽出するためにkeyだけ分離
        list=list(question2)#value側を求める為にlist化
        turth=list[self.figure]
        Q=self.question[turth]#問題文
        if pg.K_TAB:#タブキーを押したとき
            time.sleep(self.endtime)#制限時間の設定
            root=tk.Tk()
            root.title("問題")
            root.geometry(self.geo)
            label = tk.Label(root,
                            text=Q,
                            font=("Ricty Diminished",20)
                            )
            label.pack()#ここまで問題文を表示するウィンドウの設定
            button=tk.Button(root, text="回答",command=button_click)
            button.bind("<1>",button_click)#正誤判定の為にbind
            button.pack()
            entry=tk.Entry(Width=30)
            entry.insert(tk.END,"消して回答を入力してね")#回答欄の生成
            entry.pack()
            ans=entry.get()


class perfect_body:
    def __init__(self,perfectbody):
        self.perfectbody=perfectbody #初期の無敵回数の設定


class Bomb:
    def __init__(self, color, radius, vxy, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main():
    # 練習1
    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    # 練習3
    kkt = Bird("fig/6.png", 2.0, (900, 400))

    # 練習5
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)

    Text=text({"ビクティニ":"イッシュ時間No.000は？","フシギダネ":"全国図鑑No.001は？"
,"ビリリダマ":"全国図鑑No.100は？"},)

    clock = pg.time.Clock() # 練習1
    while True:
        scr.blit() # 練習2
                # 練習4
        kkt.update(scr)

        # 練習7
        bkd.update(scr)
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return
            if event.type==pg.K_DOWN:
                if event.type==pg.K_ESCAPE:
                    time.sleep(5)#エスケープキーを押した時に5秒間のポーズ
                    
        # 練習8
        if kkt.rct.colliderect(bkd.rct): # こうかとんrctが爆弾rctと重なったら
            if perfect_body==0:#無敵回数が残っているかの確認
                return
            else:
                perfect_body-=1#無敵回数を消費
                continue
        if success_point==3:
            time.sleep(10)
            tkm.showinfo("ゲームクリア")

        pg.display.update() #練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()