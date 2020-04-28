from tkinter import *
from tkinter.ttk import *
import tkinter.font as tkfont
import opens

window = Tk()

window.title("poker")

allhands = ['aa', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'a8s', 'a7s', 'a6s', 'a5s', 'a4s', 'a3s', 'a2s', 'ako', 'kk', 'kqs', 'kjs', 'kts', 'k9s', 'k8s', 'k7s', 'k6s', 'k5s', 'k4s', 'k3s', 'k2s', 'aqo', 'kqo', 'qq', 'qjs', 'qts', 'q9s', 'q8s', 'q7s', 'q6s', 'q5s', 'q4s', 'q3s', 'q2s', 'ajo', 'kjo', 'qjo', 'jj', 'jts', 'j9s', 'j8s', 'j7s', 'j6s', 'j5s', 'j4s', 'j3s', 'j2s', 'ato', 'kto', 'qto', 'jto', 'tt', 't9s', 't8s', 't7s', 't6s', 't5s', 't4s', 't3s', 't2s', 'a9o', 'k9o', 'q9o', 'j9o', 't9o', '99', '98s', '97s', '96s', '95s', '94s', '93s', '92s', 'a8o', 'k8o', 'q8o', 'j8o', 't8o', '98o', '88', '87s', '86s', '85s', '84s', '83s', '82s', 'a7o', 'k7o', 'q7o', 'j7o', 't7o', '97o', '87o', '77', '76s', '75s', '74s', '73s', '72s', 'a6o', 'k6o', 'q6o', 'j6o', 't6o', '96o', '86o', '76o', '66', '65s', '64s', '63s', '62s', 'a5o', 'k5o', 'q5o', 'j5o', 't5o', '95o', '85o', '75o', '65o', '55', '54s', '53s', '52s', 'a4o', 'k4o', 'q4o', 'j4o', 't4o', '94o', '84o', '74o', '64o', '54o', '44', '43s', '42s', 'a3o', 'k3o', 'q3o', 'j3o', 't3o', '93o', '83o', '73o', '63o', '53o', '43o', '33', '32s', 'a2o', 'k2o', 'q2o', 'j2o', 't2o', '92o', '82o', '72o', '62o', '52o', '42o', '32o', '22']

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
handentry.grid(column=0, row=3)

resultlabel = Label(window, text="enter hand", font=lg)
resultlabel.grid(column=0, row=1)

button1 = Button(window, text='Look up', command=lookuphand)
button1.grid(column=0, row=4)

rad1 = Radiobutton(window,text='BU open  ', value=1, variable=position)

rad2 = Radiobutton(window,text='SB open  ', value=2, variable=position)

rad3 = Radiobutton(window,text='BB defend', value=3, variable=position)

rad4 = Radiobutton(window,text='Nash push', value=4, variable=position)

rad5 = Radiobutton(window,text='Nash call', value=5, variable=position)

rad1.grid(column=1, row=0)

rad2.grid(column=1, row=1)

rad3.grid(column=1, row=2)

rad4.grid(column=1, row=3)

rad5.grid(column=1, row=4)

window.mainloop()