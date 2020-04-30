from tkinter import *
from tkinter.ttk import *
import tkinter.font as tkfont
import opens
import results
#import odds #comment out for gui testing
import tkinter.scrolledtext as scrolledtext

window = Tk()
# width x height + x_offset + y_offset:
window.geometry("800x600+0+0")
window.iconphoto(False, PhotoImage(file='icon.png'))
window.title("Spin & Go Helper")
#card lists
allhands = ['aa', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'a8s', 'a7s', 'a6s', 'a5s', 'a4s', 'a3s', 'a2s', 'ako', 'kk', 'kqs', 'kjs', 'kts', 'k9s', 'k8s', 'k7s', 'k6s', 'k5s', 'k4s', 'k3s', 'k2s', 'aqo', 'kqo', 'qq', 'qjs', 'qts', 'q9s', 'q8s', 'q7s', 'q6s', 'q5s', 'q4s', 'q3s', 'q2s', 'ajo', 'kjo', 'qjo', 'jj', 'jts', 'j9s', 'j8s', 'j7s', 'j6s', 'j5s', 'j4s', 'j3s', 'j2s', 'ato', 'kto', 'qto', 'jto', 'tt', 't9s', 't8s', 't7s', 't6s', 't5s', 't4s', 't3s', 't2s', 'a9o', 'k9o', 'q9o', 'j9o', 't9o', '99', '98s', '97s', '96s', '95s', '94s', '93s', '92s', 'a8o', 'k8o', 'q8o', 'j8o', 't8o', '98o', '88', '87s', '86s', '85s', '84s', '83s', '82s', 'a7o', 'k7o', 'q7o', 'j7o', 't7o', '97o', '87o', '77', '76s', '75s', '74s', '73s', '72s', 'a6o', 'k6o', 'q6o', 'j6o', 't6o', '96o', '86o', '76o', '66', '65s', '64s', '63s', '62s', 'a5o', 'k5o', 'q5o', 'j5o', 't5o', '95o', '85o', '75o', '65o', '55', '54s', '53s', '52s', 'a4o', 'k4o', 'q4o', 'j4o', 't4o', '94o', '84o', '74o', '64o', '54o', '44', '43s', '42s', 'a3o', 'k3o', 'q3o', 'j3o', 't3o', '93o', '83o', '73o', '63o', '53o', '43o', '33', '32s', 'a2o', 'k2o', 'q2o', 'j2o', 't2o', '92o', '82o', '72o', '62o', '52o', '42o', '32o', '22']
deck = ['as', 'ks', 'qs', 'js', 'ts', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s', 'ah', 'kh', 'qh', 'jh', 'th', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h', 'ad', 'kd', 'qd', 'jd', 'td', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d', 'ac', 'kc', 'qc', 'jc', 'tc', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c']

# hand lookup
fontsize = 20
lg = tkfont.Font(family="Lucida Grande", size=fontsize) # use for widgets that don't follow default font size
tkfont.nametofont('TkDefaultFont').configure(size=fontsize) # change default font size
luhand = StringVar()
luhand.set("")
position = IntVar()
position.set(1)

def lookuphand():
    hand = luhand.get().lower()
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
lookuplabel = Label(window, text="PF Lookup:", font=lg)
handentry = Entry(window, width = 4,font = lg, textvariable=luhand)
resultlabel = Label(window, text="preflop hand", font=lg, justify = "center", anchor = "center")
lookupbutton = Button(window, text='Look up', command=lookuphand, width = 7)
rad1 = Radiobutton(window,text='BU open  ', value=1, variable=position)
rad2 = Radiobutton(window,text='SB open  ', value=2, variable=position)
rad3 = Radiobutton(window,text='BB defend', value=3, variable=position)
rad4 = Radiobutton(window,text='Nash push', value=4, variable=position)
rad5 = Radiobutton(window,text='Nash call', value=5, variable=position)


# win tracking
buyinvalue = StringVar()
buyinvalue.set("")
prizepoolvalue = StringVar()
prizepoolvalue.set("")

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
        return None
    try:
        prizepool = float(prizepool)
        prizepoolvalue.set("")
    except:
        prizepoolvalue.set("inval")
        buyinvalue.set("inval")
        return None
    wl = winloss.get()

    results.add_results(buyin, prizepool, wl)
    return None

wintrackinglabel = Label(window, text="win tracking:", font=lg)


buyinlabel = Label(window, text="buyin$:", font=lg)
prizepoollabel = Label(window, text="prize$:", font=lg)
buyinentry = Entry(window, width = 5,font = lg, justify = "right", textvariable = buyinvalue)
prizepoolentry = Entry(window, width = 5,font = lg, justify = "right", textvariable = prizepoolvalue)


win = Radiobutton(window,text='W', value=1, variable=winloss)
loss = Radiobutton(window,text='L', value=0, variable=winloss)

enterresultbutton = Button(window, text='record result', command=saveresults)


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

# odds calculator gui
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

hand1oddslabel = Label(window, text="0.00%", font=lg)

hand1card1entry = Entry(window, width = 2,font = lg, justify = "left", textvariable = hand1card1)
hand1card2entry = Entry(window, width = 2,font = lg, justify = "left", textvariable = hand1card2)


flopcard1entry = Entry(window, width = 2,font = lg, justify = "left", textvariable = flopcard1)
flopcard2entry = Entry(window, width = 2,font = lg, justify = "left", textvariable = flopcard2)
flopcard3entry = Entry(window, width = 2,font = lg, justify = "left", textvariable = flopcard3)
turncardentry = Entry(window, width = 2,font = lg, justify = "left", textvariable = turncard)
rivercardentry = Entry(window, width = 2,font = lg, justify = "left", textvariable = rivercard)

hand2card1entry = Entry(window, width = 2,font = lg, justify = "left", textvariable = hand2card1)
hand2card2entry = Entry(window, width = 2,font = lg, justify = "left", textvariable = hand2card2)

hand2oddslabel = Label(window, text="0.00%", font=lg)

tielabel = Label(window, text="tie:", font=lg)

tieoddslabel = Label(window, text="0.00%", font=lg)

def calculate_odds():

    # getting input
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
    if check_cards(allcards, holecards, communitycards, fc1, fc2, fc3): return 0

    h1odds, tieodds = odds.holdem_odds(h1c1, h1c2,h2c1, h2c2, fc1, fc2, fc3, tc, rc)
    h2odds = 100 - h1odds - tieodds
    if h2odds < 0: h2odds = 0
    h1odds = h1odds
    if h1odds < 0: h1odds = 0
    hand1oddslabel.configure(text="{:3.1f}".format(h1odds) + "%")
    hand2oddslabel.configure(text="{:3.1f}".format(h2odds) + "%")
    tieoddslabel.configure(text="{:3.1f}".format(tieodds) + "%")
    return None
def invalid_cards():
    hand1oddslabel.configure(text="inval")
    hand2oddslabel.configure(text="inval")
    tieoddslabel.configure(text="inval")
    return None
def check_cards(allcards, holecards, communitycards, fc1, fc2, fc3):
    for i in holecards:
        if not i in deck:
            invalid_cards()
            return 1
    for i in communitycards:
        if not i in deck and not i == "":
            invalid_cards()
            return 1
    for i in range(1, len(communitycards)):
        if not communitycards[i] == "":
            if communitycards[i-1] == "":
                invalid_cards()
                return 1
    for i in range(len(allcards)):
        if allcards[i] == "":
            continue
        if allcards.count(allcards[i])>1:
            invalid_cards()
            return 1
    if not fc1 == "":
        if fc2 == "":
            invalid_cards()
            return 1
        if fc3 == "":
            invalid_cards()
            return 1
    return 0
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
    bet.set("")
    pot.set("")
    buyinvalue.set("")
    prizepoolvalue.set("")
    luhand.set("")
    winloss.set(0)
    position.set(1)

    hand1oddslabel.configure(text="0.00%")
    hand2oddslabel.configure(text="0.00%")
    tieoddslabel.configure(text="0.00%")
    evlabel.configure(text = "+0.0")
    resultlabel.configure(text = "preflop hand")

    return None

# EV calc gui
calculateoddsbutton = Button(window, text='calculate', command=calculate_odds)
clearcardsbutton = Button(window, text='clear', command=clear_cards)

bet = StringVar()
pot = StringVar()
# bet/pot size
evcalculatorlabel = Label(window, text="all-in EV:", font=lg)
betlabel = Label(window, text="bet:", font=lg)
potlabel = Label(window, text="pot:", font=lg)
betentry = Entry(window, width = 5,font = lg, justify = "left", textvariable = bet)
potentry = Entry(window, width = 5,font = lg, justify = "left", textvariable = pot)
evlabel = Label(window, text="+0.0", font=lg)


def calculate_ev():
    winper = float(hand1oddslabel["text"][0:-1])/100
    lossper = float(hand2oddslabel["text"][0:-1])/100
    try:
        towin = float(pot.get())
    except:
        evlabel.configure(text = "inval")
        return None
    try:
        tolose = float(bet.get())
    except:
        evlabel.configure(text = "inval")
        return None
    expectedvalue = winper*towin - lossper*tolose
    if expectedvalue >= 0:
        evlabel.configure(text = "+" + "{:.1f}".format(expectedvalue))
    else:
        evlabel.configure(text="{:.1f}".format(expectedvalue))
    print(expectedvalue)
    return None

def save_ev():
    try:
        expectedvalue = float(evlabel.cget("text"))
    except:
        evlabel.configure(text="inval")
        return
    results.add_ev(expectedvalue)
    return None


def graph_ev():
    results.display_ev(0)
    return None

calculateevbutton = Button(window, text='calculate', command=calculate_ev)

enterevbutton = Button(window, text='record EV', command=save_ev)

graphevbutton = Button(window, text='graph EV', command=graph_ev)


# progress = Progressbar(window, orient = HORIZONTAL,
#               length = 150, mode = 'determinate')
# progress.grid(column = 10, row = 5, columnspan = 5)
ysep = Separator(window, orient=VERTICAL)
ysep.place(x=400, y=0,  height = 600, anchor=NW)
lookuplabel.place(x=15, y=0, anchor=NW)
lookuplabel.place(x=15, y=0, anchor=NW)
resultlabel.place(x=100, y=80, anchor=CENTER)
handentry.place(x=65, y=110, anchor=NW)
rad1.place(x=230, y=10, anchor=NW)
rad2.place(x=230, y=50, anchor=NW)
rad3.place(x=230, y=90, anchor=NW)
rad4.place(x=230, y=130, anchor=NW)
rad5.place(x=230, y=170, anchor=NW)
lookupbutton.place(x=40, y=160, anchor=NW)
#
# wintrackinglabel.place(x=5, y=160, anchor=NW)
# buyinlabel.place(x=5, y=160, anchor=NW)
# prizepoollabel.place(x=5, y=160, anchor=NW)
# buyinentry.place(x=5, y=160, anchor=NW)
# prizepoolentry.place(x=5, y=160, anchor=NW)
# win.place(x=5, y=160, anchor=NW)
# loss.place(x=5, y=160, anchor=NW)
# enterresultbutton.place(x=5, y=160, anchor=NW)
# listresultbutton.place(x=5, y=160, anchor=NW)
# graphresultbutton.place(x=5, y=160, anchor=NW)
#
# oddscalculatorlabel.grid(column = 7, row = 0, sticky = "w")
# hand1oddslabel.grid(column = 8, row = 2, columnspan = 4, sticky = "w")
# hand1card1entry.grid(column = 8, row = 1, sticky = "w")
# hand1card2entry.grid(column = 9, row = 1, sticky = "w")
# flopcard1entry.grid(column = 10, row = 3, sticky = "w")
# flopcard2entry.grid(column = 11, row = 3, sticky = "w")
# flopcard3entry.grid(column = 12, row = 3, sticky = "w")
# turncardentry.grid(column = 13, row = 3, sticky = "w")
# rivercardentry.grid(column = 14, row = 3, sticky = "w")
# hand2card1entry.grid(column = 15, row = 1, sticky = "w")
# hand2card2entry.grid(column = 16, row = 1, sticky = "w")
# hand2oddslabel.grid(column = 15, row = 2, columnspan = 4, sticky = "w")
# tielabel.grid(column = 10, row = 0, columnspan = 4, sticky = "w")
# tieoddslabel.grid(column = 12, row = 0, columnspan = 4, sticky = "w")
# calculateoddsbutton.grid(column = 10, row = 4, columnspan = 5)
# clearcardsbutton.grid(column = 13, row = 9, columnspan = 6)
# evcalculatorlabel.grid(column = 7, row = 5, columnspan = 6, padx = 17, sticky = "w")
# betlabel.grid(column = 7, row = 6, columnspan = 4, padx = 17, sticky = "w")
# potlabel.grid(column = 7, row = 7, columnspan = 4, padx = 17, sticky = "w")
# betentry.grid(column = 8, row = 6, columnspan = 5, sticky = "w")
# potentry.grid(column = 8, row = 7, columnspan = 5, sticky = "w")
# evlabel.grid(column = 11, row = 6, rowspan = 2, columnspan = 4, sticky = "w")
# calculateevbutton.grid(column = 10, row = 8, columnspan = 5)
# enterevbutton.grid(column = 7, columnspan = 4, padx = 17, row = 8, sticky = "w")
# graphevbutton.grid(column = 7, columnspan = 4, padx = 17, row = 9, sticky = "w")

window.mainloop()