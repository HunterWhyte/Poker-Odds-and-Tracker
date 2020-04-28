# get list of all possible 2 card hands
from odds import *
import itertools as iter
#all cards

allcards = ['2c', '2h', '2d', '2s', '3c', '3h', '3d', '3s', '4c', '4h', '4d', '4s', '5c', '5h', '5d', '5s', '6c', '6h', '6d', '6s', '7c', '7h', '7d', '7s', '8c', '8h', '8d', '8s', '9c', '9h', '9d', '9s', 'tc', 'th', 'td', 'ts', 'jc', 'jh', 'jd', 'js', 'qc', 'qh', 'qd', 'qs', 'kc', 'kh', 'kd', 'ks', 'ac', 'ah', 'ad', 'as']


def all_community(h1, h2, cardsinplay):
    # generate all possible community cards
    communities = [list(x) for x in (iter.combinations(cardsinplay,5))]
    wins = 0
    ties = 0
    scenarios = 0
    for i in communities:
        result = seven_card(h1+i, h2+i)
        if result == "tie":
            ties += 1
        else:
            wins += result
    winper = wins/len(communities)
    tiesper = ties/len(communities)
    print(winper)
    return winper, tiesper

allhands = []

for x in range(len(allcards)):
    for y in range(x+1,len(allcards)):
        hand = [allcards[x], allcards[y]]
        allhands.append(hand)

allmatchups = []
for i in range(len(allhands)):
    for j in range(i+1, len(allhands)):
        matchup = [allhands[i], allhands[j]]
        cardsinplay = [allhands[i][0], allhands[i][1], allhands[j][0], allhands[j][1]]
        count = [cardsinplay.count(x) for x in cardsinplay]
        if max(count) == 1:
            allmatchups.append(matchup)

preflopLUT = {}
print(len(allmatchups))
allmatchups = allmatchups[0:1]
for i in allmatchups:
    h1 = i[0]
    h2 = i[1]
    cardsinplay = allcards.copy()
    knowncards = [h1[0], h1[1], h2[0], h2[1]]
    for i in knowncards:
        cardsinplay.remove(i)
    preflopLUT[i] = all_community(h1,h2,cardsinplay)

