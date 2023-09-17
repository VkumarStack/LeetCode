def CheckMajority(cards):
    return Equivalence(cards)[1] > len(cards) // 2

def Equivalence(cards):
    if len(cards) == 1:
        return (cards[0], 1)
    if len(cards) == 2:
        if TestCards(cards[0], cards[1]) == True:
            return (cards[0], 2)
        else:
            return (cards[0], 1)
    
    m = len(cards) // 2
    l = cards[:m]
    r = cards[m:]
    
    leftRep = Equivalence(l)
    rightRep = Equivalence(r)
    for card in r:
        if TestCards(leftRep[0], card) == True:
            leftRep = (leftRep[0], leftRep[1] + 1)
    for card in l:
        if (TestCards(rightRep[0], card)) == True:
            rightRep = (rightRep[0], rightRep[1] + 1)
    
    return leftRep if leftRep[1] > rightRep[1] else rightRep

def TestCards(a, b):
    if a == b:
        return True
    return False

print(CheckMajority(["B", "D", "B", "A", "A", "B", "B"]))