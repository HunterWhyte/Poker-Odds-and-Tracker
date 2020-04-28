from tkinter import *
from tkinter.ttk import *
import tkinter.font as tkfont
import opens
import results
import odds
import tkinter.scrolledtext as scrolledtext

window = Tk()

window.title("poker")
#card lists
allhands = ['aa', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'a8s', 'a7s', 'a6s', 'a5s', 'a4s', 'a3s', 'a2s', 'ako', 'kk', 'kqs', 'kjs', 'kts', 'k9s', 'k8s', 'k7s', 'k6s', 'k5s', 'k4s', 'k3s', 'k2s', 'aqo', 'kqo', 'qq', 'qjs', 'qts', 'q9s', 'q8s', 'q7s', 'q6s', 'q5s', 'q4s', 'q3s', 'q2s', 'ajo', 'kjo', 'qjo', 'jj', 'jts', 'j9s', 'j8s', 'j7s', 'j6s', 'j5s', 'j4s', 'j3s', 'j2s', 'ato', 'kto', 'qto', 'jto', 'tt', 't9s', 't8s', 't7s', 't6s', 't5s', 't4s', 't3s', 't2s', 'a9o', 'k9o', 'q9o', 'j9o', 't9o', '99', '98s', '97s', '96s', '95s', '94s', '93s', '92s', 'a8o', 'k8o', 'q8o', 'j8o', 't8o', '98o', '88', '87s', '86s', '85s', '84s', '83s', '82s', 'a7o', 'k7o', 'q7o', 'j7o', 't7o', '97o', '87o', '77', '76s', '75s', '74s', '73s', '72s', 'a6o', 'k6o', 'q6o', 'j6o', 't6o', '96o', '86o', '76o', '66', '65s', '64s', '63s', '62s', 'a5o', 'k5o', 'q5o', 'j5o', 't5o', '95o', '85o', '75o', '65o', '55', '54s', '53s', '52s', 'a4o', 'k4o', 'q4o', 'j4o', 't4o', '94o', '84o', '74o', '64o', '54o', '44', '43s', '42s', 'a3o', 'k3o', 'q3o', 'j3o', 't3o', '93o', '83o', '73o', '63o', '53o', '43o', '33', '32s', 'a2o', 'k2o', 'q2o', 'j2o', 't2o', '92o', '82o', '72o', '62o', '52o', '42o', '32o', '22']
allcards = ['2c', '2h', '2d', '2s', '3c', '3h', '3d', '3s', '4c', '4h', '4d', '4s', '5c', '5h', '5d', '5s', '6c', '6h', '6d', '6s', '7c', '7h', '7d', '7s', '8c', '8h', '8d', '8s', '9c', '9h', '9d', '9s', 'tc', 'th', 'td', 'ts', 'jc', 'jh', 'jd', 'js', 'qc', 'qh', 'qd', 'qs', 'kc', 'kh', 'kd', 'ks', 'ac', 'ah', 'ad', 'as']

# hand lookup

fontsize = 20
lg = tkfont.Font(family="Lucida Grande", size=fontsize) # use for widgets that don't follow default font size
tkfont.nametofont('TkDefaultFont').configure(size=fontsize) # change default font size

position = IntVar()
position.set(1)
def lookuphand():
    hand = handentry.get().lower()
    pos = position.get()
    result = ""
    if hand not in allhands:
        result = "invalid hand"
    else:
        if pos == 1:
            result = opens.bu(hand)
        if pos == 2:
            result = opens.sb(hand)
        if pos == 3:
            result = opens.bb(hand)
        if pos == 4:
            result = opens.np(hand)
        if pos == 5:
            result = opens.nc(hand)
    resultlabel.configure(text = result)

handentry = Entry(window, width = 14,font = lg)
handentry.grid(column=0, columnspan=3, row=3)

resultlabel = Label(window, text="preflop hand", font=lg)
resultlabel.grid(column=0, columnspan=3, row=1)

lookupbutton = Button(window, text='Look up', command=lookuphand)
lookupbutton.grid(column=0, columnspan=3, row=4)

rad1 = Radiobutton(window,text='BU open  ', value=1, variable=position)

rad2 = Radiobutton(window,text='SB open  ', value=2, variable=position)

rad3 = Radiobutton(window,text='BB defend', value=3, variable=position)

rad4 = Radiobutton(window,text='Nash push', value=4, variable=position)

rad5 = Radiobutton(window,text='Nash call', value=5, variable=position)

rad1.grid(column=3, columnspan=3, row=0)

rad2.grid(column=3, columnspan=3, row=1)

rad3.grid(column=3, columnspan=3, row=2)

rad4.grid(column=3, columnspan=3, row=3)

rad5.grid(column=3, columnspan=3, row=4)

# win tracking
buyinvalue = StringVar()
buyinvalue.set("")
prizepoolvalue = StringVar()
prizepoolvalue.set("")
emptylabel = Label(window, text="", font=lg)
emptylabel.grid(column = 0, row = 5)
emptylabel2 = Label(window, text="", font=lg)
emptylabel2.grid(column = 0, row = 6)

winloss = IntVar()
def saveresults():
    buyin = buyinentry.get()
    prizepool = prizepoolentry.get()
    try:
        buyin = float(buyin)
        buyinvalue.set("")
    except:
        buyinvalue.set("inval")
        prizepoolvalue.set("inval")
        return
    try:
        prizepool = float(prizepool)
        prizepoolvalue.set("")
    except:
        prizepoolvalue.set("inval")
        buyinvalue.set("inval")
        return
    wl = winloss.get()

    results.add_results(buyin, prizepool, wl)


buyinlabel = Label(window, text="buyin$:", font=lg)
prizepoollabel = Label(window, text="prize$:", font=lg)
buyinentry = Entry(window, width = 5,font = lg, justify = "right", textvariable = buyinvalue)
prizepoolentry = Entry(window, width = 5,font = lg, justify = "right", textvariable = prizepoolvalue)

buyinlabel.grid(column = 0, row = 7, sticky = "w")
prizepoollabel.grid(column = 0, row = 8, sticky = "w")
buyinentry.grid(column=1, row=7)
prizepoolentry.grid(column=1, row=8)

win = Radiobutton(window,text='W', value=1, variable=winloss)
loss = Radiobutton(window,text='L', value=0, variable=winloss)
enterresultbutton = Button(window, text='enter result', command=saveresults)
win.grid(column=3, row=7)
loss.grid(column=4, row=7)
enterresultbutton.grid(column = 3, columnspan = 2, row = 8)

def list_results():
    win = Toplevel()
    win.wm_title("resultslist")

    txt = scrolledtext.ScrolledText(win, width=20, height=40, undo = True)

    txt['font'] = ('consolas', '12')
    txt.pack(expand=True, fill='both')
    txt.grid(row=0, column=0)
    txt.insert(1.0, results.get_results())
    b = Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)
listresultbutton = Button(window, text='list results', command=list_results)
listresultbutton.grid(column = 0, columnspan = 2, row = 9, pady = 20)
def graph_results():
    buyin = buyinentry.get()
    if buyin == "all" or buyin == "":
        results.display_results(0)
        buyinvalue.set("")
        return
    try:
        buyin = float(buyin)
        buyinvalue.set("")
    except:
        buyinvalue.set("inval")
        return
    results.display_results(str(buyin))
    return
graphresultbutton = Button(window, text='graph results', command=graph_results)
graphresultbutton.grid(column = 3, columnspan = 2, row = 9)

# odds calculator

# initialize card string variables
hand1card1 = StringVar()
hand1card2 = StringVar()
hand2card1 = StringVar()
hand2card2 = StringVar()

flopcard1 = StringVar()
flopcard2 = StringVar()
flopcard3 = StringVar()
turncard  = StringVar()
rivercard = StringVar()

oddscalculatorlabel = Label(window, text="odds:", font=lg)
oddscalculatorlabel.grid(column = 7, row = 0, sticky = "w")

hand1oddslabel = Label(window, text="0.00%", font=lg)
hand1oddslabel.grid(column = 8, row = 2, columnspan = 4, sticky = "w")

hand1card1entry = Entry(window, width = 2,font = lg, justify = "left", textvariable = hand1card1)
hand1card2entry = Entry(window, width = 2,font = lg, justify = "left", textvariable = hand1card2)

hand1card1entry.grid(column = 8, row = 1, sticky = "w")
hand1card2entry.grid(column = 9, row = 1, sticky = "w")

flopcard1entry = Entry(window, width = 2,font = lg, justify = "left", textvariable = flopcard1)
flopcard2entry = Entry(window, width = 2,font = lg, justify = "left", textvariable = flopcard2)
flopcard3entry = Entry(window, width = 2,font = lg, justify = "left", textvariable = flopcard3)
turncardentry = Entry(window, width = 2,font = lg, justify = "left", textvariable = turncard)
rivercardentry = Entry(window, width = 2,font = lg, justify = "left", textvariable = rivercard)


flopcard1entry.grid(column = 10, row = 3, sticky = "w")
flopcard2entry.grid(column = 11, row = 3, sticky = "w")
flopcard3entry.grid(column = 12, row = 3, sticky = "w")
turncardentry.grid(column = 13, row = 3, sticky = "w")
rivercardentry.grid(column = 14, row = 3, sticky = "w")

hand2card1entry = Entry(window, width = 2,font = lg, justify = "left", textvariable = hand2card1)
hand2card2entry = Entry(window, width = 2,font = lg, justify = "left", textvariable = hand2card2)

hand2card1entry.grid(column = 15, row = 1, sticky = "w")
hand2card2entry.grid(column = 16, row = 1, sticky = "w")

hand2oddslabel = Label(window, text="0.00%", font=lg)
hand2oddslabel.grid(column = 15, row = 2, columnspan = 4, sticky = "w")


def calculate_odds():
    h1c1 = hand1card1.get().lower()
    h1c2 = hand1card2.get().lower()
    h2c1 = hand2card1.get().lower()
    h2c2 = hand2card2.get().lower()
    fc1 = flopcard1.get().lower()
    fc2 = flopcard2.get().lower()
    fc3 = flopcard3.get().lower()
    tc = turncard.get().lower()
    rc = rivercard.get().lower()
    allcards = [h1c1, h1c2,h2c1, h2c2, fc1, fc2, fc3, tc, rc]
    holecards = [h1c1, h1c2,h2c1, h2c2]
    communitycards = [fc1, fc2, fc3, tc, rc]
    for i in holecards:
        if not i in allcards:
            hand1oddslabel.configure(text = "inval")
            hand2oddslabel.configure(text="inval")
            return None
    for i in communitycards:
        if not i in allcards and not i == "":
            hand1oddslabel.configure(text = "inval")
            hand2oddslabel.configure(text="inval")
            return None
    for i in range(len(allcards)):
        if allcards[i] == "":
            continue
        if allcards.count(allcards[i])>1:
            hand1oddslabel.configure(text = "inval")
            hand2oddslabel.configure(text="inval")
            return None

    h1odds, tieodds = odds.holdem_odds(h1c1, h1c2,h2c1, h2c2, fc1, fc2, fc3, tc, rc)
    h2odds = 100 - h1odds - tieodds
    if h2odds < 0: h2odds = 0
    h1odds = h1odds - tieodds
    if h1odds < 0: h1odds = 0
    hand1oddslabel.configure(text="{:3.1f}".format(h1odds) + "%")
    hand2oddslabel.configure(text="{:3.1f}".format(h2odds) + "%")
    print(h1odds)
    return None

def clear_cards():
    hand1card1.set("")
    hand1card2.set("")
    hand2card1.set("")
    hand2card2.set("")

    flopcard1.set("")
    flopcard2.set("")
    flopcard3.set("")

    turncard.set("")
    rivercard.set("")

    hand1oddslabel.configure(text="0.00%")
    hand2oddslabel.configure(text="0.00%")
    return None
calculateoddsbutton = Button(window, text='calculate', command=calculate_odds)
calculateoddsbutton.grid(column = 10, row = 4, columnspan = 5)

clearcardsbutton = Button(window, text='clear', command=clear_cards)
clearcardsbutton.grid(column = 13, row = 9, columnspan = 5)
window.mainloop()