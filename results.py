import matplotlib.pyplot as plt

def add_results(buyin, prize, result):
    return

def display_results(stakes):
    """
    display chip ev, bankroll, win% for given stake
    """
    f = open("results.txt")
    games = f.read().rstrip().split("\n")
    for i in range(len(games)):
        games[i] = games[i].split(" ")
    results = []
    for i in range(len(games)):
        if stakes == "all":
            results.append(games[i])
        if games[i][0] == stakes:
            results.append(games[i])

    print(results)
    bankroll = []
    chips = []
    winloss = 0
    total = 0
    totalchips = 0
    for i in range(len(results)):
        # bankroll
        total += int(results[i][2])*float(results[i][1]) - float(results[i][0])
        bankroll.append(total)
        # chips
        if int(results[i][2]) == 0:
            totalchips += -500
        else:
            totalchips += 1000
        chips.append(totalchips)
        # win/loss
        winloss += int(results[i][2])
    winlossper = winloss/len(results)
    print(bankroll)
    print(chips)
    print(winlossper*100)
    plt.plot(bankroll)
    plt.ylabel('winnings USD$')
    plt.show()
display_results("all")