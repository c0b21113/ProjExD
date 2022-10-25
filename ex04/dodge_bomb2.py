from itertools import count
from turtle import speed
import pygame as pg
import sys
from random import randint


def check_bound(obj_rct, scr_rct):

    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main():
    # 練習1
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("ex03/fig/fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    # 練習3
    tori_sfc = pg.image.load("ex03/fig/fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    key_option=pg.key.get_pressed()
    if key_option[pg.K_1]: tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 1.0)
    if key_option[pg.K_ESCAPE]:    pg.transform.rotozoom(tori_sfc,0.1)
    
    key_option2=pg.key.get_pressed()
    if key_option[pg.K_RSHIFT]:    tori_rct.centerx*=5
    if key_option[pg.KEYUP]:    tori_rct.centerx/=2
    if key_option[pg.K_RSHIFT]:   tori_rct.centery*=5
    if key_option[pg.KEYUP]:    tori_rct.centerx/=2
    if key_option[pg.KEYUP]:    tori_rct.centery/=2
 
    # 練習5
    bomb_sfc = pg.Surface((20, 20)) # 空のSurface
    bomb_sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
    pg.draw.circle(bomb_sfc, (0, 255, 0), (10, 10), 10) # 円を描く
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)
    # 練習6
    vx, vy = +1, +1


    clock = pg.time.Clock() # 練習1
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) # 練習2
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP] or key_states[pg.K_w]:    tori_rct.centery -= 1
        if key_states[pg.K_DOWN] or key_states[pg.K_s]:  tori_rct.centery += 1
        if key_states[pg.K_LEFT] or key_states[pg.K_a]:  tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT] or key_states[pg.K_d]: tori_rct.centerx += 1
        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_states[pg.K_LEFT] or key_states[pg.K_a]: 
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT] or key_states[pg.K_d]:
                tori_rct.centerx -= 1
        if tate == -1:
            if key_states[pg.K_UP] or key_states[pg.K_w]: 
                tori_rct.centery += 1
            if key_states[pg.K_DOWN] or key_states[pg.K_s]:
                tori_rct.centery -= 1 
        scrn_sfc.blit(tori_sfc, tori_rct) # 練習3

        # 練習7
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        
        """""
        speedlist=[0.1,0.33,0.5,1.2,1.3]
        check=randint(0,1)
        if check==1:
            vx+=speedlist[randint(0,4)]
            vy+=speedlist[randint(0,4)]
        else:
            vx-=speedlist[randint(0,4)]
            if vx<0:
                vx=0.3
            vy-=speedlist[randint(0,4)]
            if vy<0:
                vy=0.3
       """ 
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx, vy) # 練習6
        scrn_sfc.blit(bomb_sfc, bomb_rct) # 練習5

        # 練習8
        if tori_rct.colliderect(bomb_rct): # こうかとんrctが爆弾rctと重なったら
            return
            

        pg.display.update() #練習2
        clock.tick(1000)

if __name__ == "__main__":
    pg.init() # 初期化
    main() # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()