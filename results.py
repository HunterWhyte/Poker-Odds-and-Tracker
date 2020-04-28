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
    played = 0
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

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    plt.suptitle(stakes + " Spin & Go Results || win% ="+ "{:8.4f}".format((winlossper*100)) + "%")
    ax1.set_xlabel('tournaments')
    ax1.set_ylabel('winnings USD', color=color)
    ax1.plot(bankroll, color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylim([0, (max(chips) + 2000)/2000])
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('chips', color=color)  # we already handled the x-label with ax1
    ax2.plot(chips, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim([0, max(chips) + 2000])
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()

display_results("0.25")