# carreau: Diamonds
# Trefle:  Clubs
# Coeur:   Heart
# Pique:   Spades

import itertools as t
from collections import Counter

values = '23456789TJQKA'
suits = 'HDCS'

STARTING = [
    ['K','Q','J','T','9','8','7','6','5','4','3','2','A'],
    [83 , 64, 64, 63, 61, 60, 59, 58, 58, 57, 56, 55, 66], # K
    [62 , 80, 61, 61, 59, 58, 56, 55, 55, 54, 53, 52, 65], # Q
    [62 , 59, 78, 59, 57, 56, 54, 53, 52, 51, 50, 50, 65], # J
    [61 , 59, 57, 75, 56, 54, 53, 51, 49, 49, 48, 47, 64], # T
    [59 , 57, 55, 53, 72, 53, 51, 50, 48, 46, 46, 45, 62], # 9
    [58 , 55, 53, 52, 50, 69, 50, 49, 47, 45, 43, 43, 61], # 8
    [57 , 54, 52, 50, 48, 47, 67, 48, 46, 45, 43, 41, 60], # 7
    [56 , 53, 50, 48, 47, 46, 45, 64, 46, 44, 42, 40, 59], # 6
    [55 , 52, 49, 47, 45, 44, 43, 43, 61, 44, 43, 41, 60], # 5
    [54 , 51, 48, 46, 43, 42, 41, 41, 41, 58, 42, 40, 59], # 4
    [54 , 50, 48, 45, 43, 40, 39, 39, 39, 38, 55, 39, 58], # 3
    [53 , 49, 47, 44, 42, 40, 37, 37, 37, 36, 35, 51, 57], # 2
    [68 , 67, 66, 66, 64, 63, 63, 62, 62, 61, 60, 59, 85]] # A

def careOfAs(card1, card2):
    card1 = 14 if card1 == 1 else card1
    card2 = 14 if card2 == 1 else card2
    if (card1 > card2):
        return True
    else:   return False

def ratingPreFlopHand(playerCards):
    if (playerCards[0][0] == playerCards[1][0]):
        return STARTING[-playerCards[0][0]][-playerCards[1][0]]
    elif (playerCards[0][1] == playerCards[1][1]):
        if (careOfAs(playerCards[0][0], playerCards[1][0])):
            return STARTING[-playerCards[0][0]][-playerCards[1][0]]
        else:
            return STARTING[-playerCards[1][0]][-playerCards[0][0]]
    else:
        if (careOfAs(playerCards[0][0], playerCards[1][0])):
            return STARTING[-playerCards[1][0]][-playerCards[0][0]]
        else:
            return STARTING[-playerCards[0][0]][-playerCards[1][0]]

def incombPlayer(nbPlayer):
    return 0
    if (nbPlayer == 1):
        return 7.1
    if (nbPlayer == 2):
        return 2 * 6.8
    if (nbPlayer == 3):
        return 3 * 6.2
    if (nbPlayer == 4):
        return 4 * 6
    if (nbPlayer == 5):
        return 5 * 5.7
    if (nbPlayer == 6):
        return 6 * 5.4
    if (nbPlayer == 7):
        return 7 * 5.1
    if (nbPlayer == 8):
        return 8 * 5
    return 0

def convertCards(playerCards, board):
    returnBoard = ""
    for index in playerCards:
        returnBoard = returnBoard + ''.join(map(str, index)) + ' '
    for index in board:
        returnBoard = returnBoard + ''.join(map(str, index)) + ' '
    returnBoard = returnBoard.replace('10', 'T')
    returnBoard = returnBoard.replace('11', 'J')
    returnBoard = returnBoard.replace('12', 'Q')
    returnBoard = returnBoard.replace('13', 'K')
    returnBoard = returnBoard.replace('1', 'A')
    return returnBoard

def value(c):
    return values.find(c[0])

def suit(c):
    return c[1]

def amounts(h):
    vals = list(map(value, h))
    return [vals.count(v) for v in set(vals)]

def score(h):
    vals = sorted(map(value, h))
    return sum(len(values)**i * v for i, v in enumerate(vals))

def straightFlush(h):
    return straight(h) and flush(h)

def fourOfAKind(h):
    return 4 in amounts(h)

def fullHouse(h):
    return 3 in amounts(h) and 2 in amounts(h)

def flush(h):
    return len(set(map(suit, h))) == 1

def straight(h):
    vals = sorted(map(value, h))
    if vals[0] == 0 and vals[-1] == len(values) - 1: #if there's a two and an ace
        vals = vals[:-1] #then remove the ace
    return map(lambda x: x + 1, vals[:-1]) == vals[1:]

def threeOfAKind(h):
    return 3 in amounts(h)

def twoPair(h):
    return amounts(h).count(2) == 2

def pair(h):
    return 2 in amounts(h)

def highCard(h):
    return True

def compare(h1, h2): #return True if h1 wins, False otherwise
    funcs = [straightFlush, fourOfAKind, fullHouse, flush, straight, threeOfAKind, twoPair, pair, highCard]
    for f in funcs:
        r1, r2 = f(h1), f(h2)
        if r1 and not r2:
            return True
        elif r2 and not r1:
            return False
        elif r1 and r2:
            s1, s2 = score(h1), score(h2)
            if s1 > s2:
                return True
            elif s2 > s1:
                return False
    return False #tie case

def bestHand(cards):
    hands = list(t.combinations(cards, 5))
    bestHand = hands[0]
    for h in hands:
        if compare(h, bestHand):
            bestHand = h
    return bestHand

def find_most_occ_char(input):
    inp = input.replace('C', '')
    inp = inp.replace('S', '')
    inp = inp.replace('H', '')
    inp = inp.replace('D', '')
    inp = inp.replace(' ', '')
    return Counter(inp).most_common(1)[0][1]

def deflactorHand(cards):
    if (find_most_occ_char(cards) == 4):
        return 0
    else:
        return 2

def handClassement(cards, nbPlayer):
    visible = cards.split()
    table = tuple(visible[2:])
    visible = set(visible)
    deck = set([c[0] + c[1] for c in t.product(values, suits)]) - visible
    hand = bestHand(visible)
    wins = 0
    total = 0
    for c1 in deck:
        for c2 in deck:
            if c1 == c2:
                break
            otherHand = bestHand(table + (c1, c2))
            if compare(hand, otherHand):
                wins += 1
            total += 1
    return ((float(wins) / total)) * 100 - incombPlayer(nbPlayer) - deflactorHand(cards)

def getPair(cards, nbCards):
    occur = Counter(cards).most_common(1)[0][1]
    if (occur >= 2):
        return True
    if (len(cards) == 5):
        return (6.0 / nbCards) + (6.0 / (nbCards - 1)) - ((6.0 / nbCards) * (6.0 / (nbCards - 1)))
    if (len(cards) == 6):
        return (6.0 / nbCards)

def getDbPair(cards, nbCards):
    occu1 = Counter(cards).most_common(1)[0]
    if (occu1[1] >= 2):
        tmp = [x for x in cards if x != occu1[0]]
        occu2 = Counter(tmp).most_common(1)[0]
        if (occu2[1] >= 2):
            return True
        if (len(cards) == 5):
            return ((len(tmp) * 3) / nbCards) + ((len(tmp) * 3) / (nbCards - 1)) - (((len(tmp) * 3) / nbCards) * ((len(tmp) * 3) / (nbCards - 1)))
        if (len(cards) == 6):
            return ((len(tmp) * 3) / nbCards)
    occur = Counter(cards).most_common(1)[0][1]
    if (occur == 1):
        if (len(cards) == 5):
            return pow((6.0 / nbCards) + (6.0 / (nbCards - 1)) - ((6.0 / nbCards) * (6.0 / (nbCards - 1))), 2)
        if (len(cards) == 6):
            return 0
    if (occur >= 2):
        if (len(cards) == 5):
            return (6.0 / nbCards) + (6.0 / (nbCards - 1)) - ((6.0 / nbCards) * (6.0 / (nbCards - 1)))
        if (len(cards) == 6):
            return (6.0 / nbCards)

def getBrelan(cards, nbCards):
    outs = Counter(cards).most_common(1)[0][1]
    if (outs >= 3):
        return True
    else:
        if (outs == 1):
            return ((4 - outs) / nbCards) * ((3 - outs) / (nbCards - 1))
        outs = 4 - outs
        probaFlop = (outs) / nbCards
        probaRiver = (outs) / (nbCards - 1)
        if (len(cards) == 5):
            return (probaFlop + probaRiver) - (probaFlop * probaRiver)
        if (len(cards) == 6):
            return (outs) / nbCards

def getFlush(cards, nbCards):
    occur = Counter(cards).most_common(1)[0][1]
    if (occur >= 5):
        return True
    else:
        outs = 13 - occur
        probaFlop = (outs) / nbCards
        probaRiver = (outs) / (nbCards - 1)
        if (len(cards) == 5):
            if (occur == 3):
                return ((13 - occur) / nbCards) * ((12 - occur) / (nbCards - 1))
            elif (occur == 4):
                return (probaFlop + probaRiver) - (probaFlop * probaRiver)
            else:   return 0
        if (len(cards) == 6):
            if (occur == 4):
                return (outs) / nbCards
            else:
                return 0

def getFull(cards, nbCards):
    return 0

def getSquare(cards, nbCards):
    outs = Counter(cards).most_common(1)[0][1]
    if (outs >= 4):
        return True
    elif (outs == 1):
        return 0
    else:
        if (outs == 2):
            return ((4 - outs) / nbCards) * ((3 - outs) / (nbCards - 1))
        outs = 4 - outs
        probaFlop = (outs) / nbCards
        probaRiver = (outs) / (nbCards - 1)
        if (len(cards) == 5):
            return (probaFlop + probaRiver) - (probaFlop * probaRiver)
        if (len(cards) == 6):
            return (outs) / nbCards

def getStraight(cards, nbCards):
    cnt = 0
    cnt2 = 0
    tmp = sorted(cards)
    for x, index in enumerate(tmp[:-1]):
        if (index + 1 == tmp[x + 1]):
            cnt += 1
    for i, j in enumerate(tmp):
        if j == 1:
            tmp[i] = 14
    tmp = sorted(tmp)
    for x, index in enumerate(tmp[:-1]):
        if (index + 1 == tmp[x + 1]):
            cnt2 += 1
    if (cnt < cnt2):
        cnt = cnt2
    occur = cnt + 1
    if (occur >= 5):
        return True
    if (occur < 3):
        return 0
    if (len(cards) == 5):
        if (occur == 4):
            probaFlop = (4) / nbCards
            probaRiver = (4) / (nbCards - 1)
            return (probaFlop + probaRiver) - (probaFlop * probaRiver)
        if (occur == 3):
            return (4 / nbCards) * (4 / (nbCards - 1))
    if (len(cards) == 6):
        if (occur != 4):
            return 0
        return (4.0 / nbCards)

def cleanCards(cards, index):
    tmp = []
    for i in cards:
        tmp.append(i[index])
    return tmp

def getProba(cards, nbCards):
    return  (getPair(cleanCards(cards, 0), nbCards),
            getDbPair(cleanCards(cards, 0), nbCards),
            getBrelan(cleanCards(cards, 0), nbCards),
            getSquare(cleanCards(cards, 0), nbCards),
            getFlush(cleanCards(cards, 1), nbCards),
            getStraight(cleanCards(cards, 0), nbCards))

#print (getProba([[1, 'H'], [3, 'C'], [4, 'D'], [1, 'D'], [1, 'C']] , 58 - 8))