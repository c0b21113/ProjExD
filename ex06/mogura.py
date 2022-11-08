
import pygame as pg
import sys
from random import randint


class Screen:#スクリーンの設定
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg)
        self.bgi_rct = self.bgi_sfc.get_rect()     
        
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Hole:#穴の画像を20個生成
    def __init__(self,visial,topleftx,toplefty):
        sfc= pg.image.load(visial) # "fig/6.png"
        self.sfc= pg.transform.scale(sfc, (200,180))#画像のサイズ調整
        self.rct = self.sfc.get_rect()
        self.rct.topleft = topleftx,toplefty#座標の設定
 
    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)


class Mole:#モグラの生成
    def __init__(self,visial,centerx,centery):
        sfc= pg.image.load(visial) #画像の指定
        self.sfc= pg.transform.scale(sfc, (90,70))#サイズ指定
        self.rct = self.sfc.get_rect()
        self.rct.bottomleft = centerx,centery#座標の設定

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)      

    def update(self,scr:Screen):#モグラが徐々に上ってくる様に更新
        a,b=self.rct.bottomleft
        random1=randint(1,10)
        random2=randint(1,20)
        if random1==1:#ランダムがヒットした時、10だけ上に上がる
            b-=10
            self.rct.bottomleft=(a,b)#座標の更新
        elif random2==10:#ランダムがヒットした時、5だけ下に下がる
            b-=5
            self.rct.bottomleft=(a,b)#座標の更新
        self.blit(scr)



def main():
    hole_list=[]
    mole_list=[]
    scr = Screen("モグラ", (1600, 900),"ダウンロード/jpg")#背景の設定
    for i in range(5):
        for j in range(4):
            mole_list.append(Mole("jpeg置き場/9572.png",120+290*(i),200+190*(j)))
            hole_list.append(Hole("jpeg置き場/hole_ana.png",100+290*(i),100+190*(j)))
#リストに穴とネズミを格納
    clock = pg.time.Clock() # 練習1
    while True:
        scr.blit()
        for i in range(20):
            mole_list[i].update(scr)#ネズミを先に描画
            hole_list[i].blit(scr)#穴を後に描画することで隠す
            
        pg.display.update() #アップデート
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()
