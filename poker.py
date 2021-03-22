# ["PreFlop", [10, 'D'], [10, 'C']]

import proba_poker as prbP

Player = "player"
PreFlop = "preFlop"
Flop = "flop"
Turn = "turn"
River = "river"
case = [PreFlop, Flop, Turn, River, Player]

class Poker:
    def __init__(self, nbPlayer):
        self.nbPlayer = nbPlayer - 1
        self.equity = 0
        self.nbCard = 52 - (self.nbPlayer) * 2
        self.playerCard = []
        self.board = []
        self.allProba = []
    def printParams(self):
        print ("nb Cards:       {}".format(self.nbCard))
        print ("Player cards:   {}".format(self.playerCard))
        print ("Board:          {}".format(self.board))
        print ("Equity:         {}%".format(self.equity))
        if (len(self.board) < 3 or len(self.board) > 4):
            return
        print ("P(Pair):        {}%".format(self.allProba[0] * 100))
        print ("P(Db Pair):     {}%".format(self.allProba[1] * 100))
        print ("P(Brelan):      {}%".format(self.allProba[2] * 100))
        print ("P(Square):      {}%".format(self.allProba[3] * 100))
        print ("P(Flush):       {}%".format(self.allProba[4] * 100))
        print ("P(Straight):    {}%".format(self.allProba[5] * 100))
    def getEquity(self):
        if (self.equity == 100 or self.equity == 0):
            return sum(self.allProba)
        return  self.equity
    def getPair(self):
        return self.allProba[0] * 100
    def getDPair(self):
        return self.allProba[1] * 100
    def getBrelan(self):
        return self.allProba[2] * 100
    def getSquare(self):
        return self.allProba[3] * 100
    def getFlush(self):
        return self.allProba[4] * 100
    def getStraight(self):
        return self.allProba[5] * 100
    def getCard(self, listOfValue):
        if (listOfValue[0] not in listOfValue):
            print ("Don't know")
            return
        self.nbCard -= len(listOfValue[1:])
        if (listOfValue[0] in [Flop, Turn, River]):
            self.nbCard -= 1
        if (listOfValue[0] == PreFlop):
            self.playerCard = listOfValue[1:]
            self.equity = prbP.ratingPreFlopHand(self.playerCard)
        if (listOfValue[0] == Flop):
            self.board = listOfValue[1:]
            self.equity = int(prbP.handClassement(prbP.convertCards(self.playerCard, self.board), self.nbPlayer))
            self.allProba = prbP.getProba(self.playerCard + self.board, self.nbCard)
            return
        if (listOfValue[0] == Turn):
            self.board.append(listOfValue[1])
            self.equity = int(prbP.handClassement(prbP.convertCards(self.playerCard, self.board), self.nbPlayer))
            self.allProba = prbP.getProba(self.playerCard + self.board, self.nbCard)
            return
        if (listOfValue[0] == River):
            self.board.append(listOfValue[1])
            self.equity = int(prbP.handClassement(prbP.convertCards(self.playerCard, self.board), self.nbPlayer))
            return
