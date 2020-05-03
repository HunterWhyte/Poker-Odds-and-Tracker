from tkinter import *
from tkinter.ttk import *
import tkinter.font as tkfont
import opens
import results
#import odds #comment out for gui testing
import tkinter.scrolledtext as scrolledtext

window = Tk()
# width x height + x_offset + y_offset:
window.geometry("800x500+0+0")
window.iconphoto(False, PhotoImage(file='icon.png'))
window.title("Spin & Go Helper")
#card lists
allhands = ['aa', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'a8s', 'a7s', 'a6s', 'a5s', 'a4s', 'a3s', 'a2s', 'ako', 'kk', 'kqs', 'kjs', 'kts', 'k9s', 'k8s', 'k7s', 'k6s', 'k5s', 'k4s', 'k3s', 'k2s', 'aqo', 'kqo', 'qq', 'qjs', 'qts', 'q9s', 'q8s', 'q7s', 'q6s', 'q5s', 'q4s', 'q3s', 'q2s', 'ajo', 'kjo', 'qjo', 'jj', 'jts', 'j9s', 'j8s', 'j7s', 'j6s', 'j5s', 'j4s', 'j3s', 'j2s', 'ato', 'kto', 'qto', 'jto', 'tt', 't9s', 't8s', 't7s', 't6s', 't5s', 't4s', 't3s', 't2s', 'a9o', 'k9o', 'q9o', 'j9o', 't9o', '99', '98s', '97s', '96s', '95s', '94s', '93s', '92s', 'a8o', 'k8o', 'q8o', 'j8o', 't8o', '98o', '88', '87s', '86s', '85s', '84s', '83s', '82s', 'a7o', 'k7o', 'q7o', 'j7o', 't7o', '97o', '87o', '77', '76s', '75s', '74s', '73s', '72s', 'a6o', 'k6o', 'q6o', 'j6o', 't6o', '96o', '86o', '76o', '66', '65s', '64s', '63s', '62s', 'a5o', 'k5o', 'q5o', 'j5o', 't5o', '95o', '85o', '75o', '65o', '55', '54s', '53s', '52s', 'a4o', 'k4o', 'q4o', 'j4o', 't4o', '94o', '84o', '74o', '64o', '54o', '44', '43s', '42s', 'a3o', 'k3o', 'q3o', 'j3o', 't3o', '93o', '83o', '73o', '63o', '53o', '43o', '33', '32s', 'a2o', 'k2o', 'q2o', 'j2o', 't2o', '92o', '82o', '72o', '62o', '52o', '42o', '32o', '22']
deck = ['as', 'ks', 'qs', 'js', 'ts', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s', 'ah', 'kh', 'qh', 'jh', 'th', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h', 'ad', 'kd', 'qd', 'jd', 'td', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d', 'ac', 'kc', 'qc', 'jc', 'tc', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c']

# hand lookup
fontsize = 18
lg = tkfont.Font(family="TkDefaultFont", size=fontsize) # use for widgets that don't follow default font size
tkfont.nametofont('TkDefaultFont').configure(size=fontsize) # change default font size
luhand = StringVar()
luhand.set("")
position = StringVar()
position.set("BB")
action = IntVar()
action.set(1)
players = IntVar()
players.set(3)
# TODO: add 2H and 3H options. Add Position options the separate scenario options for each posisition(BU limps SB 2.5x etc)
def lookuphand():
    hand = luhand.get().lower()
    pos = position.get()

    result = ""
    if hand not in allhands:
        result = "invalid hand"
        return None

    resultlabel.configure(text = result)
    return None
handentry = Entry(window, width = 4,font = lg, textvariable=luhand)
resultlabel = Label(window, text="preflop hand", font=lg, justify = "center", anchor = "center")
lookupbutton = Button(window, text='lookup', command=lookuphand, width = 7)

BB = Radiobutton(window,text='BB', value="BB", variable=position)
SB = Radiobutton(window,text='SB', value="SB", variable=position)
BU = Radiobutton(window,text='BU', value="BU", variable=position)
nash = Radiobutton(window,text='nash eq', value="n", variable=position)

action1 = Radiobutton(window,text='', value=1, variable=action)
action2 = Radiobutton(window,text='', value=2, variable=action)
action3 = Radiobutton(window,text='', value=3, variable=action)
action4 = Radiobutton(window,text='', value=4, variable=action)

def set_position():
    n = players.get()
    pos = position.get()
    act = action.get()
    if n == 2:
        BB.place(x=145, y=30, anchor=NW)
        BU.place(x=200, y=30, anchor=NW)
        BU.configure(text = "BU")
        SB.place(x=0, y=0, anchor = SE)
        nash.place(x=255, y=30, anchor=NW)
        if pos == "n":
            action.set(1)
            action1.configure(text="push")
            action2.configure(text="call")
            action1.place(x=210, y=100, anchor=NW)
            action2.place(x=210, y=140, anchor=NW)
            action3.place(x=0, y=0, anchor=SE)
            action4.place(x=0, y=0, anchor=SE)

        if pos == "SB":
            pos = "BU"
            position.set(pos)
        if pos == "BU":
            action.set(1)
            action1.configure(text = "opening")
            action1.place(x = 210, y =100, anchor = NW)
            action2.place(x=0, y=0, anchor = SE)
            action3.place(x=0, y=0, anchor = SE)
            action4.place(x=0, y=0, anchor=SE)

        if pos == "BB":
            action.set(1)
            action1.configure(text = "BU limps")
            action2.configure(text="BU raises")
            action1.place(x = 210, y =100, anchor = NW)
            action2.place(x=210, y=140, anchor = NW)
            action3.place(x=0, y=0, anchor = SE)
            action4.place(x=0, y=0, anchor=SE)

    if n == 3:
        BB.place(x=145, y=30, anchor=NW)
        SB.place(x=200, y=30, anchor=NW)
        BU.place(x=255, y=30, anchor=NW)
        nash.place(x=0, y=0, anchor=SE)
        BU.configure(text = "BU")
        if pos == "SB":
            action.set(1)
            action1.configure(text="BU min-raise")
            action2.configure(text="BU folds")
            action1.place(x=210, y=100, anchor=NW)
            action2.place(x=210, y=140, anchor=NW)
            action3.place(x=0, y=0, anchor = SE)
            action4.place(x=0, y=0, anchor=SE)

        if pos == "BU":
            action.set(1)
            action1.configure(text = "opening")
            action1.place(x = 210, y =100, anchor = NW)
            action2.place(x=0, y=0, anchor = SE)
            action3.place(x=0, y=0, anchor = SE)
            action4.place(x=0, y=0, anchor=SE)

        if pos == "BB":
            action.set(1)
            action1.configure(text="BU min-raise")
            action2.configure(text="SB 2.5x raise")
            action3.configure(text="BU limps")
            action4.configure(text="SB limps")
            action1.place(x=210, y=100, anchor=NW)
            action2.place(x=210, y=140, anchor=NW)
            action3.place(x=210, y=180, anchor=NW)
            action4.place(x=210, y=220, anchor=NW)


set_position()

twohanded = Radiobutton(window, text = "2H", value = 2, variable = players, command = set_position)
twohanded.place(x = 75, y = 30, anchor = NW)
threehanded = Radiobutton(window, text = "3H", value = 3, variable = players, command = set_position)
threehanded.place(x = 5, y = 30, anchor = NW)

playerslabel = Label(window, text="players:", font=lg)
playerslabel.place(x=15, y=0, anchor=NW)
playersysep = Separator(window, orient=VERTICAL)
playersysep.place(x=135, y=0,  height =65, anchor=NW)
playershsep = Separator(window, orient=HORIZONTAL)
playershsep.place(x=0, y=65,  width = 400, anchor=NW)

positionlabel = Label(window, text="position:", font=lg)
positionlabel.place(x=150, y=0, anchor=NW)

preflopactionlabel = Label(window, text="preflop action:", font=lg)
preflopactionlabel.place(x=210, y=65, anchor=NW)
preflopactionysep = Separator(window, orient=VERTICAL)
preflopactionysep.place(x=200, y=65,  height =185, anchor=NW)
preflopactionhsep = Separator(window, orient=HORIZONTAL)
preflopactionhsep.place(x=0, y=65,  width = 400, anchor=NW)

BB.configure(command = set_position)
SB.configure(command = set_position)
BU.configure(command = set_position)
nash.configure(command = set_position)


resultlabel.place(x=105, y=100, anchor=CENTER)
handentry.place(x=65, y=125, anchor=NW)
lookupbutton.place(x=35, y=170, anchor=NW)





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


buyinlabel = Label(window, text="buyin:", font=lg)
prizepoollabel = Label(window, text="prize:", font=lg)
buyinentry = Entry(window, width = 5,font = lg, justify = "right", textvariable = buyinvalue)
prizepoolentry = Entry(window, width = 5,font = lg, justify = "right", textvariable = prizepoolvalue)


win = Radiobutton(window,text='W', value=1, variable=winloss)
loss = Radiobutton(window,text='L', value=0, variable=winloss)

enterresultbutton = Button(window, text='record result', command=saveresults, width = 12)


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

def graph_results():
    stakes = graphstakes.get()
    if stakes == "all" or stakes == "":
        results.display_results(0)
        return None
    try:
        stakes = float(stakes)
    except:
        graphstakes.set("inval")
        return None
    results.display_results(str(stakes))
    return None
graphresultbutton = Button(window, text='graph results', command=graph_results, width =12)
graphresultslabel = Label(window, text = "display results:")
stakeslabel = Label(window, text = "stakes:")
graphstakes = StringVar()
graphstakesentry = Entry(window, textvariable= graphstakes, font = lg, width = 5, justify = "right")
listresultbutton = Button(window, text='list results', command=list_results, width = 12)

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
    graphstakes.set("")
    hand1oddslabel.configure(text="0.00%")
    hand2oddslabel.configure(text="0.00%")
    tieoddslabel.configure(text="0.00%")
    evlabel.configure(text = "+0.0")
    resultlabel.configure(text = "preflop hand")
    luhand.set("")
    position.set("BB")
    action.set(1)
    players.set(3)

    return None

# EV calc gui
calculateoddsbutton = Button(window, text='calculate', command=calculate_odds)
clearcardsbutton = Button(window, text='clear all', command=clear_cards)

bet = StringVar()
pot = StringVar()
# bet/pot size
evcalculatorlabel = Label(window, text="all-in EV:", font=lg)
betlabel = Label(window, text="bet:", font=lg)
potlabel = Label(window, text="pot:", font=lg)
betentry = Entry(window, width = 4,font = lg, justify = "left", textvariable = bet)
potentry = Entry(window, width = 4,font = lg, justify = "left", textvariable = pot)
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

calculateevbutton = Button(window, text='calculate', command=calculate_ev, width = 9)

enterevbutton = Button(window, text='record EV', command=save_ev, width = 9)

graphevbutton = Button(window, text='graph EV', command=graph_ev, width = 9)


def increasefont():
    global fontsize, lg ,tkfont
    fontsize += 1
    lg.configure(size=fontsize)   # use for widgets that don't follow default font size
    tkfont.nametofont('TkDefaultFont').configure(size=fontsize)  # change default font size
    return None


def decreasefont():
    global fontsize, lg ,tkfont
    fontsize += -1
    lg.configure(size=fontsize) # use for widgets that don't follow default font size
    tkfont.nametofont('TkDefaultFont').configure(size=fontsize)  # change default font size
    return None

increasefontbutton = Button(window, text='font size +', command=increasefont, width = 11)
decreasefontbutton = Button(window, text='font size -', command=decreasefont, width = 11)

#
ysep = Separator(window, orient=VERTICAL)
ysep.place(x=400, y=0,  height = 500, anchor=NW)
ysepleft = Separator(window, orient=VERTICAL)
ysepleft.place(x=1, y=0,  height = 500, anchor=NW)
ysepright = Separator(window, orient=VERTICAL)
ysepright.place(x=799, y=0,  height = 500, anchor=NW)
hsep = Separator(window, orient=HORIZONTAL)
hsep.place(x=0, y=250,  width = 800, anchor=NW)
hseptop = Separator(window, orient=HORIZONTAL)
hseptop.place(x=0, y=1,  width = 800, anchor=NW)
hsepbottom = Separator(window, orient=HORIZONTAL)
hsepbottom.place(x=0, y=499,  width = 800, anchor=NW)

#

#
hsep2 = Separator(window, orient=HORIZONTAL)
hsep2.place(x=0, y=385,  width = 800, anchor=NW)
wintrackinglabel.place(x=5, y=250, anchor=NW)
buyinlabel.place(x=5, y=285, anchor=NW)
prizepoollabel.place(x=5, y=325, anchor=NW)
buyinentry.place(x=100, y=285, anchor=NW)
prizepoolentry.place(x=100, y=325, anchor=NW)
win.place(x=230, y=285, anchor=NW)
loss.place(x=320, y=285, anchor=NW)
enterresultbutton.place(x=205, y=320, anchor=NW)
#
listresultbutton.place(x=205, y=390, anchor=NW)
graphresultbutton.place(x=205, y=440, anchor=NW)
graphresultslabel.place(x=5, y=390, anchor=NW)
graphstakesentry.place(x=100, y=440, anchor=NW)
stakeslabel.place(x=5, y=440, anchor=NW)
oddsposition = 415
oddscalculatorlabel.place(x=405, y=0, anchor=NW)
hand1card1entry.place(x=oddsposition, y=50, anchor=NW)
hand1card2entry.place(x=oddsposition+40, y=50, anchor=NW)
hand1oddslabel.place(x=oddsposition, y=90, anchor=NW)
flopcard1entry.place(x=oddsposition+90, y=120, anchor=NW)
flopcard2entry.place(x=oddsposition+130, y=120, anchor=NW)
flopcard3entry.place(x=oddsposition+170, y=120, anchor=NW)
turncardentry.place(x=oddsposition+210, y=120, anchor=NW)
rivercardentry.place(x=oddsposition+250, y=120, anchor=NW)
hand2card1entry.place(x=oddsposition+290, y=50, anchor=NW)
hand2card2entry.place(x=oddsposition+330, y=50, anchor=NW)
hand2oddslabel.place(x=oddsposition+290, y=90, anchor=NW)
tielabel.place(x=oddsposition+120, y=60, anchor=NW)
tieoddslabel.place(x=oddsposition+170, y=60, anchor=NW)
calculateoddsbutton.place(x=oddsposition+110, y=170, anchor=NW)

#
evcalculatorlabel.place(x=405, y=250, anchor=NW)
betlabel.place(x=410, y=290, anchor=NW)
potlabel.place(x=410, y=330, anchor=NW)
betentry.place(x=465, y=290, anchor=NW)
potentry.place(x=465, y=330, anchor=NW)
evlabel.place(x=540, y=310, anchor=NW)
calculateevbutton.place(x=650, y=250, anchor=NW)
enterevbutton.place(x=650, y=295, anchor=NW)
graphevbutton.place(x=650, y=340, anchor=NW)
clearcardsbutton.place(x=405, y=390, anchor=NW)
increasefontbutton.place(x=600, y=390, anchor=NW)
decreasefontbutton.place(x=600, y=440, anchor=NW)

s = Style()
s.theme_use('default')

window.mainloop()