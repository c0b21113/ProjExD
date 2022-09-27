global lost_alp,chance,ans


import random
import datetime
import copy

all_alp=26
celect_alp=12
lost_alp=2
celected_alp=[]
ans=[]


def Question():

    celected_alp=[]
    ans=[]
    for i in range(20):
        celected_alp.append(chr(random.randint(65,90)))
        if len(celected_alp)>12:
            break
#12つの文字をUnicodeからの変換で求めています
    copys=copy.deepcopy(celected_alp)
    ans.append(celected_alp.pop(random.randint(1,12)))
    ans.append(celected_alp.pop(random.randint(1,11)))
#其のうち2つの文字を別のリストに追加しています
    Copy1=random.shuffle(copys)
    print(copys)
    print(celected_alp)

        
def Answer():
    chance=0
    while True:
        n=int(input("欠損文字はいくつでしょうか"))
        if n==lost_alp:
            print("正解です")
            break
        else:
            print("不正解です")
            continue
    while chance<3:
        ans1=input("1つ目の欠損した文字を答えてください")
        ans2=input("2つ目の欠損した文字を答えてください")
        if ans1 in ans:
            print("正解")
            break
        if ans2 in ans or ans1 in ans:
            print("どちらか一方は正解です,もう一度回答してください")
            chance+=1
        else:
            print("何方も不正解です、もう一度回答してください")
            chance+=1
#不具合で100％間違える様になっています                
Question()
Answer()