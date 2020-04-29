suits = ["s" , "h", "d", "c"]

cards = ["a","k","q","j","t","9","8","7","6","5","4","3","2"]
cardmapping = []
for i in range(len(suits)):
    suit = suits[i]
    for i in range(len(cards)):
        card = cards[i]
        cardmapping.append(card+suit)

print(cardmapping)