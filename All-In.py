#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
from pygame import mixer
from random import randint
import blackJack as bj
import poker as pk

for index, name in enumerate(sr.Microphone.list_microphone_names()): print("Microphone with name \"{1}\" found for Microphone(device_index={0})".format(index, name))

r = sr.Recognizer()
quit = 0
frame = 0
myCard = 0
dealerCard = 0
otherCard = 0
cardSprite = []
blackjackClass = bj.BlackJack(0)
pokerClass = pk.Poker(6)


def exitAll(window):
    global quit

    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter ?"):
        window.destroy()
        quit = 1


def frameSwap(window, i):
    global frame
    window.destroy()

    frame = i

def upBar(window):
    menubar = tk.Menu(window)

    barButton = tk.Menu(menubar, tearoff=0)
    barButton.add_command(label="Menu", command=lambda: frameSwap(window, 0))
    barButton.add_command(label="Poker", command=lambda: frameSwap(window, 1))
    barButton.add_command(label="BlackJack", command=lambda: frameSwap(window, 2))
    barButton.add_command(label="Quitter", command=lambda: exitAll(window))
    menubar.add_cascade(label="Menu", menu=barButton)

    helpButton = tk.Menu(menubar, tearoff=0)
    helpButton.add_command(label="A propos")
    menubar.add_cascade(label="Aide", menu=helpButton)

    window.config(menu=menubar)


def getCardNumber(text):
    if "as" in text:
         return 1
    if "3" in text or "trois" in text:
        return 3
    if "4" in text or "quatre" in text or "cadre" in text:
        return 4
    if "5" in text or "cinq" in text:
        return 5
    if "6" in text or "six" in text or "fils" in text:
        return 6
    if "7" in text or "set" in text or "sept" in text:
        return 7
    if "8" in text or "huit" in text:
        return 8
    if "9" in text or "neuf" in text:
        return 9
    if "10" in text or "dix" in text:
        return 10
    if "valet" in text or "valais" in text:
        return 11
    if "dame" in text:
        return 12
    if "roi" in text or "rot" in text:
        return 13
    if "2" in text or "deux" in text or "peu" in text or "de" in text:
        return 2
    return 84


def getCardType(text):
    if "pique" in text or "pik" in text:
        return 's'
    if "carreau" in text:
        return 'd'
    if "trèfle" in text:
        return 'c'
    if "cœur" in text:
        return 'h'

    type = randint(1, 4)
    if type == 1:
        return 's'
    elif type == 2:
        return 'h'
    elif type == 3:
        return 'd'
    else:
        return 'c'


def getCardTypePoker(text):
    if "pique" in text or "pik" in text:
        return 's'
    if "carreau" in text:
        return 'd'
    if "trèfle" in text:
        return 'c'
    if "cœur" in text:
        return 'h'
    return 84


def getWho(text):
    if "croupier" in text or "copier" in text:
        return "croupier"
    if "j'ai" in text or "moi" in text or "g" in text or "-" in text or "moins" in text:
        return "moi"
    if "autre" in text or "notre" in text:
        return "autre"
    if "remise à zéro" in text:
        return "full reset"
    if "recommence" in text:
        return "reset"
    return "erreur"


def getWhoPoker(text):
    if "j'ai" in text or "moi" in text or "g" in text or "preflop" in text or "pre flop" in text or "-" in text or "moins" in text:
        return "moi"
    if "flop" in text:
        return "flop"
    if "turn" in text or "terme" in text:
        return "turn"
    if "river" in text:
        return "river"
    if "remise à zéro" in text:
        return "full reset"
    if "recommence" in text:
        return "reset"
    return "erreur"


def printThatCardBlackjack(window, canvas, text):
    global myCard
    global dealerCard
    global otherCard
    global cardSprite
    global blackjackClass
    text = text.lower()

    blackjackClass.debugParams()
    print("Text:\t%s" % text)

    who = getWho(text)
    number = getCardNumber(text)
    type = getCardType(text)

    if who == "erreur":
        return 84

    i = 0
    if who == "reset":
        while i < len(cardSprite):
            canvas.delete(cardSprite[i])
            i += 1
        canvas.delete("textResult")
        blackjackClass.getCards("reset")
        myCard = 0
        dealerCard = 0
        otherCard = 0
        return 0

    if who == "full reset":
        while i < len(cardSprite):
            canvas.delete(cardSprite[i])
            i += 1
        canvas.delete("textResult")
        blackjackClass.getCards("full_reset")
        myCard = 0
        dealerCard = 0
        otherCard = 0
        return 0

    if number != 84:
        file1 = './pictures/cards/'
        file2 = file1 + type
        file3 = file2 +  str(number)
        file4 = file3 + '.gif'
        card = tk.PhotoImage(file=file4)
        print (file4)
        if who == "moi":
            cardSprite.append(canvas.create_image(915 + myCard * 15, 780, image=card, anchor='nw'))
            myCard += 1
            idResult = blackjackClass.getCards(["moi", number])
        elif who == "croupier":
            cardSprite.append(canvas.create_image(915 + dealerCard * 15, 120, image=card, anchor='nw'))
            dealerCard += 1
            idResult = blackjackClass.getCards(["croupier", number])
        else:
            cardSprite.append(canvas.create_image(1615, 120 + 30 * otherCard, image=card, anchor='nw'))
            otherCard += 1
            idResult = blackjackClass.getCards(["autre", number])
        canvas.delete("textResult")
        if idResult == 0:
            canvas.create_text(960, 495, fill="white", font="Fixedsys 50 bold", text="...", tag="textResult")
        elif idResult == 'R':
            canvas.create_text(960, 495, fill="white", font="Fixedsys 50 bold", text="Stop", tag="textResult")
        elif idResult == 'S':
            canvas.create_text(960, 495, fill="white", font="Fixedsys 50 bold", text="Split", tag="textResult")
        elif idResult == 'D':
            canvas.create_text(960, 495, fill="white", font="Fixedsys 50 bold", text="Double", tag="textResult")
        elif idResult == 'T':
            canvas.create_text(960, 495, fill="white", font="Fixedsys 50 bold", text="Tire", tag="textResult")
        else:
            canvas.create_text(960, 495, fill="white", font="Fixedsys 50 bold", text=idResult, tag="textResult")

        window.mainloop()
        return 0
    return 84


def printThatCardPoker(window, canvas, text):
    global myCard
    global dealerCard
    global otherCard
    global cardSprite
    global pokerClass
    text = text.lower()

    print(text)
    loop = 0
    who = getWhoPoker(text)

    if who == "erreur":
        return 84

    i = 0
    if who == "reset":
        while i < len(cardSprite):
            canvas.delete(cardSprite[i])
            i += 1
        canvas.delete("textResult")
        canvas.delete("textResult0")
        canvas.delete("textResult1")
        canvas.delete("textResult2")
        canvas.delete("textResult3")
        canvas.delete("textResult4")
        canvas.delete("textResult5")
        myCard = 0
        dealerCard = 0
        otherCard = 0
        pokerClass.reset()
        return 0

    if who == "full reset":
        while i < len(cardSprite):
            canvas.delete(cardSprite[i])
            i += 1
        canvas.delete("textResult")
        canvas.delete("textResult0")
        canvas.delete("textResult1")
        canvas.delete("textResult2")
        canvas.delete("textResult3")
        canvas.delete("textResult4")
        canvas.delete("textResult5")
        myCard = 0
        dealerCard = 0
        otherCard = 0
        pokerClass.reset()
        return 0

    array = text.split(" et ")
    card1array = []
    card2array = []
    card3array = []

    while loop < len(array):
        text = array[loop]
        print (text)
        number = getCardNumber(text)
        type = getCardTypePoker(text)

        if type == 84:
            return 84

        if number != 84:
            file1 = './pictures/cards/'
            file2 = file1 + type
            file3 = file2 +  str(number)
            file4 = file3 + '.gif'
            if loop == 0:
                card1 = tk.PhotoImage(file=file4)
                card1array.append(number)
                card1array.append(type.upper())
            elif loop == 1:
                card2 = tk.PhotoImage(file=file4)
                card2array.append(number)
                card2array.append(type.upper())
            else:
                card3 = tk.PhotoImage(file=file4)
                card3array.append(number)
                card3array.append(type.upper())
            print (file4)
            if who == "moi":
                if loop == 0:
                    cardSprite.append(canvas.create_image(890 + myCard * 80, 100, image=card1, anchor='nw'))
                elif loop == 1:
                    cardSprite.append(canvas.create_image(890 + myCard * 80, 100, image=card2, anchor='nw'))
                    pokerClass.getCard(["preFlop", [card1array[0], card1array[1]], [card2array[0], card2array[1]]])
                myCard += 1
                if myCard >= 2:
                    break
            else:
                if loop == 0:
                    cardSprite.append(canvas.create_image(765 + dealerCard * 80, 450, image=card1, anchor='nw'))
                    if who == "turn":
                        pokerClass.getCard(["turn", [card1array[0], card1array[1]]])
                    elif who == "river":
                        pokerClass.getCard(["river", [card1array[0], card1array[1]]])
                if loop == 1:
                    cardSprite.append(canvas.create_image(765 + dealerCard * 80, 450, image=card2, anchor='nw'))
                if loop == 2:
                    cardSprite.append(canvas.create_image(765 + dealerCard * 80, 450, image=card3, anchor='nw'))
                    pokerClass.getCard(["flop", [card1array[0], card1array[1]], [card2array[0], card2array[1]], [card3array[0], card3array[1]]])
                dealerCard += 1
                if dealerCard >= 5:
                    break
        loop += 1
    canvas.delete("textResult")
    canvas.delete("textResult0")
    canvas.delete("textResult1")
    canvas.delete("textResult2")
    canvas.delete("textResult3")
    canvas.delete("textResult4")
    canvas.delete("textResult5")


    equity = str(pokerClass.getEquity()) + "%"
    canvas.create_text(960, 425, fill="#EFAE05", font="Fixedsys 30 bold", text=equity, tag="textResult")

    if who != "moi":
        equity0 = "Paire " + str(round(pokerClass.getPair(), 2)) + "%"
        equity1 = "2 Paires " + str(round(pokerClass.getDPair(), 2)) + "%"
        equity2 = "Brelan " + str(round(pokerClass.getBrelan(), 2)) + "%"
        equity3 = "Carré " + str(round(pokerClass.getSquare(), 2)) + "%"
        equity4 = "Couleur " + str(round(pokerClass.getFlush(), 2)) + "%"
        equity5 = "Suite " + str(round(pokerClass.getStraight(), 2)) + "%"
        print(equity1)
        canvas.create_text(1710, 75, fill="#EFAE05", font="Fixedsys 30 bold", text=equity0, tag="textResult0")
        canvas.create_text(1710, 125, fill="#EFAE05", font="Fixedsys 30 bold", text=equity1, tag="textResult1")
        canvas.create_text(1710, 175, fill="#EFAE05", font="Fixedsys 30 bold", text=equity2, tag="textResult2")
        canvas.create_text(1710, 225, fill="#EFAE05", font="Fixedsys 30 bold", text=equity3, tag="textResult3")
        canvas.create_text(1710, 275, fill="#EFAE05", font="Fixedsys 30 bold", text=equity4, tag="textResult4")
        canvas.create_text(1710, 325, fill="#EFAE05", font="Fixedsys 30 bold", text=equity5, tag="textResult5")


    pokerClass.printParams()
    window.mainloop()
    return 0


def voiceBlackjack(window, canvas):
    with sr.Microphone(device_index= None) as source:
        audio = r.listen(source, phrase_time_limit=2)
    try:
        text = r.recognize_google(audio, language="fr-FR")
        if printThatCardBlackjack(window, canvas, text) == 84:
            mixer.init()
            mixer.music.load('error.mp3')
            mixer.music.play()
            print("Error")
    except Exception:
        return
    return


def voicePoker(window, canvas):
    with sr.Microphone(device_index= None) as source:
        audio = r.listen(source, phrase_time_limit=5)
    try:
        text = r.recognize_google(audio, language="fr-FR")
        if printThatCardPoker(window, canvas, text) == 84:
            mixer.init()
            mixer.music.load('error.mp3')
            mixer.music.play()
            print("Error")
    except Exception:
        return
    return


def blackjack(window, canvas):
    global myCard
    global dealerCard
    global otherCard

    myCard = 0
    dealerCard = 0
    otherCard = 0
    tkImg = tk.PhotoImage(file='./pictures/blackjack.gif')
    canvas.create_image(0, 0, image=tkImg, anchor='nw')
    talkButton = tk.Button(window, text="Jouer", command=lambda: voiceBlackjack(window, canvas), anchor='center',
                                activebackground="#098002", height=2, width=6, font=("Arial", 25, "bold"))
    canvas.create_window(265, 140, anchor='nw', window=talkButton)
    window.mainloop()


def poker(window, canvas):
    global myCard
    global dealerCard
    global otherCard

    myCard = 0
    dealerCard = 0
    otherCard = 0
    tkImg = tk.PhotoImage(file='./pictures/poker.gif')
    canvas.create_image(-90, -550, image=tkImg, anchor='nw')
    talkButton = tk.Button(window, text="Jouer", command=lambda: voicePoker(window, canvas), anchor='center',
                                activebackground="#098002", height=3, width=16, font=("Arial", 25, "bold"))
    canvas.create_window(959, 855, anchor='center', window=talkButton)
    window.mainloop()


def menu(window, canvas):
    global myCard
    global dealerCard
    global otherCard

    myCard = 0
    dealerCard = 0
    otherCard = 0
    tkImg = tk.PhotoImage(file='./pictures/WSOP2.gif')
    canvas.create_image(0, 0, image=tkImg, anchor='nw')
    pokerButton = tk.Button(window, text="Poker", command=lambda: frameSwap(window, 1), anchor='center', activebackground="#ED012A", height=4, width=20, font=("Arial",25,"bold"))
    canvas.create_window(960, 290, anchor='center', window=pokerButton)
    blackjackButton = tk.Button(window, text="BlackJack", command=lambda: frameSwap(window, 2), anchor='center',
                                activebackground="#ED012A", height=4, width=20, font=("Arial", 25, "bold"))
    canvas.create_window(960, 690, anchor='center', window=blackjackButton)
    window.mainloop()


def mainMenu():
    global myCard
    global dealerCard
    global otherCard

    myCard = 0
    dealerCard = 0
    otherCard = 0

    window = tk.Tk()
    window.title("All - In")
    window.protocol("WM_DELETE_WINDOW", lambda :exitAll(window))
    canvas = tk.Canvas(window, width=1920, height=1080)
    canvas.pack()

    upBar(window)
    menu(window, canvas)


def mainPoker():
    window = tk.Tk()
    window.title("All - In")
    window.protocol("WM_DELETE_WINDOW", lambda :exitAll(window))
    canvas = tk.Canvas(window, width=1920, height=1080)
    canvas.pack()

    upBar(window)
    poker(window, canvas)
    window.mainloop()


def mainBlackjack():
    window = tk.Tk()
    window.title("All - In")
    window.protocol("WM_DELETE_WINDOW", lambda :exitAll(window))
    canvas = tk.Canvas(window, width=1920, height=1080)
    canvas.pack()

    upBar(window)
    blackjack(window, canvas)
    window.mainloop()


def mainGame():
    global frame
    global quit

    while quit == 0:
        if frame == 0:
            mainMenu()
        if frame == 1:
            mainPoker()
        if frame == 2:
            mainBlackjack()


def main():
    mainGame()
    return


if __name__ == '__main__':
    main()
