#!/usr/bin/python3

from sys import exit
import proba

STOP = "stop"
DEALER = "croupier"
ME = "moi"
OTHER = "autre"
RESET = "reset"
FULL_RESET = "full_reset"

class BlackJack:
    def __init__(self, nbCards):
        self.nbCards = 0 #nbCards
        self.compt = 0
        self.cumPond = 1
        self.realCompt = self.compt / self.cumPond
        self.cards = []
        self.dealerCards = 0
        self.playerCards = []
    def debugParams(self):
        print("Nb cards:     {}".format(self.nbCards))
        print("Cards:        {}".format(self.cards))
        print("PLayer Cards: {}".format(self.playerCards))
        print("Dealer Cards: {}".format(self.dealerCards))
        print("Compt:        {}".format(self.compt))
        print("Cm:           {}".format(self.cumPond))
        print("RealCompt:    {}".format(self.realCompt))
    ##### DEBUG #####
    def getRealCompt(self):
        return self.realCompt
    def getDealerCard(self):
        return self.dealerCards
    def getNbCard(self):
        return self.nbCards
    def getLenCards(self):
        return len(self.cards)
    def getLenPlayer(self):
        return len(self.playerCards)
    def getCumPond(self):
        return self.cumPond
    #################
    def reset(self):
        del self.playerCards[:]
        self.dealerCards = 0
    def fullReset(self):
        self.reset()
        del self.cards[:]
        self.compt = 0
        self.nbCards = 0
        self.cumPond = 1
        self.realCompt = self.compt / self.cumPond
    def setCm(self):
        if (self.nbCards >= 52 * 0):
            self.cumPond = 1
        if (self.nbCards > 52 * 1):
            self.cumPond = 2
        if (self.nbCards > 52 * 2):
            self.cumPond = 3
        if (self.nbCards > 52 * 3):
            self.cumPond = 4
        if (self.nbCards > 52 * 4):
            self.cumPond = 5
        if (self.nbCards > 52 * 5):
            self.cumPond = 6
    def setCompt(self, cards):
        if (cards in [2, 3, 4, 5, 6]):
            self.compt += 1
        elif (cards in [10, 11, 12, 13, 1]):
            self.compt -= 1
        elif (cards in [7, 8, 9]):
            pass
        else:
            print ("ERROR")
    def specialOption(self, special):
        if (special == RESET):
            self.reset()
            return True
        if (special == FULL_RESET):
            self.fullReset()
            return True
        return False
    def calcProba(self):
        if (len(self.playerCards) < 2 or self.dealerCards == 0):
            return False
        elif (1 in self.playerCards):
            return proba.caseAs(self.playerCards, self.dealerCards, self.realCompt)
        elif (proba.isPair(self.playerCards)):
            return proba.casePair(self.playerCards, self.dealerCards, self.realCompt)
        else:   return proba.caseNormal(self.playerCards, self.dealerCards, self.realCompt)
    def setParams(self, cards):
        self.cards.append(cards)
        self.nbCards += 1
        self.setCm()
        self.setCompt(cards)
        self.realCompt = int(self.compt / self.cumPond)
    def getCards(self, pair):
        if (len(pair) != 2):
            return self.specialOption(pair)
        pair[1] = int(pair[1])
        self.setParams(pair[1])
        if (pair[0] == DEALER and self.dealerCards == 0):
            self.dealerCards = pair[1]
        if (pair[0] == ME):
            self.playerCards.append(pair[1])
        if (pair[0] == OTHER):
            pass
        ret = self.calcProba()
        if (ret == 'D' and len(self.playerCards) > 2):
            ret = 'T'
        return ret