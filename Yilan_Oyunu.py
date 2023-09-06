import turtle
import time
import random


# oyun ekranı oluşturma
oyunEkranı = turtle.Screen()
oyunEkranı.tracer(0)
oyunEkranı.setup(600,600)  # pencere boyutu
oyunEkranı.bgcolor("black")  # pencere rengi


# Yılan oluşturuldu
yılan = turtle.Turtle()
yılan.shape("square")  # yılanın şekli
yılan.color("white")  # yılanın rengi
yılan.speed(0)   # yılanın yenilenme animasyon hızı
yılan.penup()  # yılanın arkasındaki izi siliyor
yılan.goto(-200,0)  # yılanın başlicağı kordinat
yılan.yön = "dur"


# Yılanın yemi oluşturuldu
yem = turtle.Turtle()
yem.shape("square")  # yemin şekli
yem.color("yellow")  # yemin rengi
yem.speed(0)   # yemin yenilenme animasyon hızı
yem.penup()  # yemin arkasındaki izi siliyor
yem.goto(0,0)  # yemin başlicağı kordinat
yem.yön = "dur"


# Yılanın yönünü hareket ettiren fonksiyonlar
def yukarı():
    if yılan.yön != "aşağı":
        yılan.yön = "yukarı"

def aşağı():
    if yılan.yön != "yukarı":
        yılan.yön = "aşağı"

def sağa():
    if yılan.yön != "sol":
        yılan.yön = "sağ"

def sola():
    if yılan.yön != "sağ":
        yılan.yön = "sol"


# klavyeden gelen hareketler
oyunEkranı.listen()  # klavyeden gelen hareketler
oyunEkranı.onkeypress(yukarı, "w")  # fonksiyonu çalıştırır değer girmek yerine harf atatdık
oyunEkranı.onkeypress(aşağı, "s")
oyunEkranı.onkeypress(sola, "a")
oyunEkranı.onkeypress(sağa, "d")


# ok tuşları
oyunEkranı.onkeypress(yukarı, "Up")  # fonksiyonu çalıştırır değer girmek yerine harf atatdık
oyunEkranı.onkeypress(aşağı, "Down")
oyunEkranı.onkeypress(sağa, "Right")
oyunEkranı.onkeypress(sola, "Left")


# hareket etmesi için fonk tanımlanıcak
def hareket_et():
    if yılan.yön == "yukarı":
        y = yılan.ycor()
        yılan.sety(y + 20)  # yılanın var olan y kordinatını alıyorum 20 artırıyorum

    if yılan.yön == "aşağı":
        y = yılan.ycor()
        yılan.sety(y - 20)  # yılanın var olan y kordinatını alıyorum 20 eksiltiyorum
    
    if yılan.yön == "sağ":
        x = yılan.xcor()
        yılan.setx(x + 20)  # yılanın var olan x kordinatını alıyorum 20 artırıyorum
    
    if yılan.yön == "sol":
        x = yılan.xcor()
        yılan.setx(x - 20)  # yılanın var olan x kordinatını alıyorum 20 eksiltiyorum
    
    

bolumler = []

while True:
    oyunEkranı.update()

    if yılan.xcor() > 290 or yılan.xcor() < -290 or yılan.ycor() > 290 or yılan.ycor() < -290:  # bu if yılanın çarpıcağı
        time.sleep(1) # yılan çıkarsa oyunu 1 sn durdur                                       # 4 köşe ile ilgili
        yılan.goto(-200,0)  # yılan başlangıç kordinatlarına geri gel
        yılan.yön = "dur"

        for i in bolumler:
            i.goto(2000,2000)
        
        bolumler.clear()


    if yılan.distance(yem) < 20:
        x = random.randint(-290,290)  # hareket ediceği piksel oranı
        y = random.randint(-290,290)
        yem.goto(x,y)

        yeniBolum = turtle.Turtle()
        yeniBolum.speed(0)  # hız 0
        yeniBolum.shape("square")  # şekil kare
        yeniBolum.penup()  # şeklin arkasındaki izleri kaybeder
        yeniBolum.color("white")
        bolumler.append(yeniBolum)


    for i in range(len(bolumler)-1,0,-1):
        x = bolumler[i-1].xcor()
        y = bolumler[i-1].ycor()
        bolumler[i].goto(x,y)


    if len(bolumler) > 0:
        x = yılan.xcor()
        y = yılan.ycor()
        bolumler[0].goto(x,y)


    hareket_et()
    

    for i in bolumler:
        if i.distance(yılan) < 20:
            time.sleep(1)
            yılan.goto(-200,0)
            yılan.yön = "dur"

            for i in bolumler:
                i.goto(2000,2000)
            
            bolumler.clear()



    time.sleep(0.1)  # yılanın hızı

    # yılan oyunu