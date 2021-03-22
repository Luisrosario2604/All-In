normal = [      # DOUBLER SI COMPT >= x else Tirer
    ['T', 'T', 'T', 'T', 'T' ,'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T'], # 5 #
    ['T', 'T', 'T', 'T', 'T' ,'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T'], # 6 #
    ['T', 'T', 'T', 'T', 'T' ,'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T'], # 7 #
    ['T', 'T', 'T', 'T', 'T' ,'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T'], # 8 #
    ['T', +3, 0, 0, -3 ,-3, +3, +6, 'T', 'T', 'T', 'T,', 'T'],         # 9 #
    [+3, +3, 'D', 'D', 'D', 'D', -3, -3, 0, +3, +3, +3, +3],           # 10 #
    [0, 'D', 'D', 'D', 'D', 'D', 'D', -3, -3, -3, -3, -3, -3],         # 11 #
                # RESTER SI COMPT >= X else TIRER
    ['T', +3, 0, 0, 0, -3, 'T', 'T', 'T', 'T', 'T', 'T', 'T'],         # 12 #
    ['T', 0, 0, -3, -3, -6, 'T', 'T', 'T', 'T', 'T', 'T', 'T'],        # 13 #
    ['T', -3, -3, -3, -6, 'R', 'T', 'T', 'T', 'T', 'T', 'T', 'T'],     # 14 #
    [+3, -3, -6, -6, 'R', 'R', 'T', +6, +6, +3, +3, +3, +3],           # 15 #
    [+3, -6, 'R', 'R', 'R', 'R', +3, +3, +3, 0, 0, 0, 0],              # 16 #
    [-3, 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],  # 17 #
    ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'], # 18 #
    ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'], # 19 #
    ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'], # 20 #
    ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']] # 21 #

pair = [     # SPLIT SI COMPT >= x else rester
    ['T', 0, -3, 'S', 'S', 'S', 'S', +3, 'T', 'T', 'T', 'T', 'T'],     # 2-2 #
    ['T', 0, -3, 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T'],    # 3-3 #
    ['T', 'T', +3, 0, 0, -3, 'T', 'T', 'T', 'T', 'T', 'T', 'T'],       # 4-4 #
    [+3, +3, 'D', 'D', 'D', 'D', -3, -3, 0, +3, +3, +3, +3],           # 5-5 #
    ['T', 'S', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'T'], # 6-6 #
    ['T', 'S', 'S', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T'], # 7-7 #
    ['T', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T'], # 8-8 #
    [+3, 0, -3, -3, 'S', 'S', +3, 'S', 'S', 'R', 'R', 'R', 'R'],       # 9-9 #
    ['R', 'R', +6, +6, +3, +3, 'R', 'R', 'R', 'R', 'R', 'R', 'R'],     # 10-10 #
    ['R', 'R', +6, +6, +3, +3, 'R', 'R', 'R', 'R', 'R', 'R', 'R'],     # 11-11 #
    ['R', 'R', +6, +6, +3, +3, 'R', 'R', 'R', 'R', 'R', 'R', 'R'],     # 12-12 #
    ['R', 'R', +6, +6, +3, +3, 'R', 'R', 'R', 'R', 'R', 'R', 'R']]     # 13-13 #

As = [        # SPLIT SI COMPT >= x else rester
    [-3, 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],  # A-A #
    ['T', 'T', 'T', 'T', 'D', 'D', 'T', 'T', 'T', 'T', 'T', 'T', 'T'], # A-2 #
    ['T', 'T', 'T', 'T', 'D', 'D', 'T', 'T', 'T', 'T', 'T', 'T', 'T'], # A-3 #
    ['T', 'T', 'T', 'D', 'D', 'D', 'T', 'T', 'T', 'T', 'T', 'T', 'T'], # A-4 #
    ['T', 'T', 'T', 'D', 'D', 'D', 'T', 'T', 'T', 'T', 'T', 'T', 'T'], # A-5 #
    ['T', 'T', 'D', 'D', 'D', 'D', 'T', 'T', 'T', 'T', 'T', 'T', 'T'], # A-6 #
    ['T', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'T', 'T', 'T', 'T', 'T'], # A-7 #
    ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'], # A-8 #
    ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'], # A-9 #
    ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'], # A-10 #
    ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'], # A-11 #
    ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'], # A-12 #
    ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']] # A-13 #

BUST = "bust"

def casePair(playerCards, dealerCards, compt):
    if (playerCards[0] > 10):
        playerCards[0] = 10
    out = pair[playerCards[0] - 1][dealerCards - 1]
    if (isinstance(out, int)):
        if (compt >= out):
            return 'S'
        else:
            return 'R'
    else:
        return out

def caseNormal(playerCards, dealerCards, compt):
    simple = [10 if x > 10 else x for x in playerCards]
    som = sum(simple)
    if (som > 21):
        return BUST
    out = normal[som - 5][dealerCards - 1]
    if (som <= 11):
        if (isinstance(out, int)):
            if (compt >= out):
                return 'D'
            else:
                return 'T'
        else:
            return out
    else:
        if (isinstance(out, int)):
            if (compt >= out):
                return 'R'
            else:
                return 'T'
        else:
            return out

def caseAs(playerCards, dealerCards, compt):
    simple = [10 if x > 10 else x for x in playerCards]
    som = sum ([x for x in simple if x != 1])
    if (som > 21):
        return BUST
    if (som == 0 or playerCards.count(1) > 1):
        som += (playerCards.count(1) - 1)
    out = As[som - 1][dealerCards - 1]
    if (isinstance(out, int)):
        if (compt >= out):
            return 'S'
        else:
            return 'R'
    else:
        return out

def isPair(playerCards):
    if (len(playerCards) != 2):
        return False
    if (playerCards[0] == playerCards[1]):
        return True
    if (playerCards[0] in range(10, 14) and playerCards[1] in range(10, 14)):
        return True
    return False