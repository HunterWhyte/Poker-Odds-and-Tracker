import matplotlib.pyplot as plt

def add_results(buyin, prize, result):
    f = open("results.txt", "a")
    f.write(str(buyin) + " " + str(prize) + " " + str(result) + "\n")
    f.close()
    return
def get_results():
    f = open("results.txt")
    resultstext = f.read()
    f.close()
    return resultstext
def display_results(stakes):
    """
    display chip ev, bankroll, win% for given stake
    """
    f = open("results.txt")
    games = f.read().rstrip().split("\n")
    f.close()
    for i in range(len(games)):
        games[i] = games[i].split(" ")
    results = []
    for i in range(len(games)):
        if stakes == 0:
            results.append(games[i])
        elif float(games[i][0]) == float(stakes):
            results.append(games[i])
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
    if winloss>0:
        winlossper = winloss/len(results)
    else:
        fig, ax = plt.subplots()
        plt.suptitle("no data available for these stakes")
        plt.show()
        return

    fig, ax1 = plt.subplots()
    fig.subplots_adjust(top=0.2)
    color = 'tab:red'
    if stakes == 0:
        stakes = "all"
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
    return
