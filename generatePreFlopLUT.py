# get list of all possible 2 card hands
from odds import *
import itertools as iter
#all cards

allcards = ['2c', '2h', '2d', '2s', '3c', '3h', '3d', '3s', '4c', '4h', '4d', '4s', '5c', '5h', '5d', '5s', '6c', '6h', '6d', '6s', '7c', '7h', '7d', '7s', '8c', '8h', '8d', '8s', '9c', '9h', '9d', '9s', 'tc', 'th', 'td', 'ts', 'jc', 'jh', 'jd', 'js', 'qc', 'qh', 'qd', 'qs', 'kc', 'kh', 'kd', 'ks', 'ac', 'ah', 'ad', 'as']
cardmapping = ['as', 'ks', 'qs', 'js', 'ts', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s', 'ah', 'kh', 'qh', 'jh', 'th', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h', 'ad', 'kd', 'qd', 'jd', 'td', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d', 'ac', 'kc', 'qc', 'jc', 'tc', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c']

def all_community(h1, h2, cardsinplay):
    # generate all possible community cards
    communities = [list(x) for x in (iter.combinations(cardsinplay,5))]
    wins = 0
    ties = 0
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

for x in range(len(cardmapping)):
    for y in range(x+1,len(cardmapping)):
        hand = [cardmapping[x], cardmapping[y]]
        allhands.append(hand)

allmatchups = []
for i in range(len(allhands)):
    for j in range(i+1, len(allhands)):
        matchup = allhands[i] + allhands[j]
        cardsinplay = [allhands[i][0], allhands[i][1], allhands[j][0], allhands[j][1]]
        count = [cardsinplay.count(x) for x in cardsinplay]
        if max(count) == 1:
            allmatchups.append(matchup)

preflopLUT = {}
print(len(allmatchups))
f = open("cards.txt", 'w')

allmatchups = allmatchups
for i in range(410000, len(allmatchups)):
    for j in range(len(allmatchups[i])):
        allmatchups[i][j] = cardmapping.index(allmatchups[i][j])
    f.write(str(allmatchups[i][0]) + str("\n")+str(allmatchups[i][1]) + str("\n")+str(allmatchups[i][2]) + str("\n")+str(allmatchups[i][3]) + str("\n"))
print(len(allmatchups))
f.close()

# for i in allmatchups:
#     h1 = i[0:2]
#     h2 = i[2:4]
#     print(h1)
#     print(h2)
#     cardsinplay = allcards.copy()
#     knowncards = [h1[0], h1[1], h2[0], h2[1]]
#     for i in knowncards:
#         cardsinplay.remove(i)
#     preflopLUT[i] = all_community(h1,h2,cardsinplay)

