import itertools as iter
import time
from joblib import Parallel, delayed
allcards = ['as', 'ks', 'qs', 'js', 'ts', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s', 'ah', 'kh', 'qh', 'jh', 'th', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h', 'ad', 'kd', 'qd', 'jd', 'td', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d', 'ac', 'kc', 'qc', 'jc', 'tc', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c']
#generate preflop LUT
possiblehands = []
for x in range(len(allcards)):
    for y in range(x+1,len(allcards)):
        hand = [allcards[x], allcards[y]]
        possiblehands.append(hand)
allmatchups = []
for i in range(len(possiblehands)):
    for j in range(i+1, len(possiblehands)):
        matchup = possiblehands[i] + possiblehands[j]
        cardsinplay = [possiblehands[i][0], possiblehands[i][1], possiblehands[j][0], possiblehands[j][1]]
        count = [cardsinplay.count(x) for x in cardsinplay]
        if max(count) == 1:
            allmatchups.append(matchup)

preflopLUT = {}
f  = open("matchups.txt", "r")
matchups = f.read().rstrip().split("\n")
f.close()
for i in range(len(matchups)):
    matchups[i] = matchups[i].split(" ")
for i in range(len(possiblehands)):
    preflopLUT[allmatchups[i]] = matchups[i]
    # 1712304 total matches

print(len(allmatchups))
print(len(preflopLUT))
def preflop(h1,h2):
    try:
        result = preflopLUT[h1+h2]
        winsper = 100*float(result[0])/1712304
        tiesper = 100*float(result[1])/1712304
        return winsper, tiesper
    except:
        result = preflopLUT[h2+h1]
        result = preflopLUT[h1+h2]
        winsper = 100 - 100*float(result[0])/1712304
        tiesper = 100*float(result[1])/1712304
        return winsper, tiesper

def seven_card(h1,h2):
    # params: seven card poker hands
    h1options = [list(x) for x in iter.combinations(h1, 5)]
    h2options = [list(x) for x in iter.combinations(h2, 5)]
    blank, hand1 = poker(h1options)
    blank, hand2 = poker(h2options)
    result, hand = poker([hand1, hand2])
    if result == 0:
        return 2
    elif result == 1:
        return hand == hand1

def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    result = [x for x in hands if hand_rank(x) == hand_rank(max(hands, key=hand_rank))]
    if len(result) > 1:
        return 0, result[0]
    else:
        return 1, result[0]

def hand_rank(hand):
    groups = group(["--23456789tjqka".index(r) for r,s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14,5,4,3,2):
        ranks = (5,4,3,2,1)
    straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4
    flush = len(set([s for r,s in hand])) == 1
    return max(count_rankings[counts], 4*straight +5*flush), ranks
count_rankings = {(5,):10,
                  (4,1):7,
                  (3,2):6,
                  (3,1,1):3,
                  (2,2,1):2,
                  (2,1,1,1):1,
                  (1,1,1,1,1):0}
def group(items):
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)
def unzip(pairs):
    return zip(*pairs)

def winloss(h1,h2,communities):
    ties=0
    wins=0
    results = Parallel(n_jobs=-1,verbose=10)(delayed(seven_card)(h1 + i, h2 + i)for i in communities)
    for result in results:
        if result == 2:
            ties += 1
        elif result == 1:
            wins += 1
    return wins, ties
# def winlossnonp(h1,h2,communities):
#     ties=0
#     wins=0
#     results = (seven_card(h1 + i, h2 + i)for i in communities)
#     for result in results:
#         if result == 2:
#             ties += 1
#         elif result == 1:
#             wins += 1
#     return wins, ties
def holdem_odds(h1c1, h1c2,h2c1, h2c2, fc1, fc2, fc3, tc, rc):
    cards = [h1c1, h1c2,h2c1, h2c2, fc1, fc2, fc3, tc, rc]
    knowncards = [x for x in cards if x != ""]

    cardsinplay = allcards.copy()
    for i in knowncards:
        cardsinplay.remove(i)
    if fc1 == "":
        print("preflop")
        h1 = [h1c1, h1c2]
        h2 = [h2c1, h2c2]
        return preflop(h1, h2)

    elif tc == "":
        print("flop")
        communities = [list(x) for x in (iter.combinations(cardsinplay, 2))]
        h1 = [h1c1, h1c2, fc1, fc2, fc3]
        h2 = [h2c1, h2c2, fc1, fc2, fc3]
        #start = time.time()
        wins,ties = winloss(h1,h2,communities)
        #print(time.time()-start)
        winper = wins/ len(communities)
        tiesper = ties / len(communities)
        return winper*100, tiesper*100
    elif rc == "":
        print("turn")
        communities = [[x] for x in cardsinplay]
        h1 = [h1c1, h1c2, fc1, fc2, fc3, tc]
        h2 = [h2c1, h2c2, fc1, fc2, fc3, tc]
        #start = time.time()
        wins,ties = winloss(h1,h2,communities)
        #print(time.time()-start)
        winper = wins / len(communities)
        tiesper = ties / len(communities)
        return winper*100, tiesper*100
    else:
        print("river")
        h1 = [h1c1, h1c2, fc1, fc2, fc3, tc, rc]
        h2 = [h2c1, h2c2, fc1, fc2, fc3, tc, rc]
        result = seven_card(h1, h2)
        if result == 2:
            return 0, 100
        elif result == 1:
            return 100, 0
        else:
            return 0,0
    return 0
