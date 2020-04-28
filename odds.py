import itertools as iter

allcards = ['2c', '2h', '2d', '2s', '3c', '3h', '3d', '3s', '4c', '4h', '4d', '4s', '5c', '5h', '5d', '5s', '6c', '6h', '6d', '6s', '7c', '7h', '7d', '7s', '8c', '8h', '8d', '8s', '9c', '9h', '9d', '9s', 'tc', 'th', 'td', 'ts', 'jc', 'jh', 'jd', 'js', 'qc', 'qh', 'qd', 'qs', 'kc', 'kh', 'kd', 'ks', 'ac', 'ah', 'ad', 'as']

def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    result = [x for x in hands if hand_rank(x) == hand_rank(max(hands, key=hand_rank))]
    if len(result) > 1:
        return 0, result[0]
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
def seven_card(h1,h2):
    # params: seven card poker hands
    h1options = [list(x) for x in iter.combinations(h1, 5)]
    h2options = [list(x) for x in iter.combinations(h2, 5)]
    blank, hand1 = poker(h1options)
    blank, hand2 = poker(h2options)
    result, hand = poker([hand1, hand2])
    if result == 0:
        return "tie"
    if result == 1:
        return hand == hand1

def test():
    "Test cases for the functions in poker program"
    # sf = "6C 7C 8C 9C TC".lower().split()
    # fk = "9D 9H 9S 9C 7D".lower().split()
    # fh = "TD TC TH 7C 7D".lower().split()
    # tp = "5S 5D 9H 9C 6S".lower().split()
    # assert poker([sf, fk, fh]) == sf
    # assert poker([fh, fk]) == fk
    # assert poker([fh, fh]) == "tie"
    # assert poker([sf]) == sf
    # assert poker([sf] + 99 * [fh]) == sf
    return None

def holdem_odds(h1c1, h1c2,h2c1, h2c2, fc1, fc2, fc3, tc, rc):
    odds = 100
    tieodds = 5.3
    cards = [h1c1, h1c2,h2c1, h2c2, fc1, fc2, fc3, tc, rc]
    knowncards = [x for x in cards if x != ""]

    availablecards = allcards
    for i in knowncards:
        availablecards.remove(i)

    return odds, tieodds
