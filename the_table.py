import uuid
from Blackjack import deckengine as de

'''
'''




deck = de.Deck()
#for card in deck.cards:
#    print(card)
player1 = de.Player('Sucker',bankroll=200)
dealer = de.Dealer()
deck.shuffle()
player1.turn = True

while True:
    player1.make_bet()
    if player1.chips.bet > 0:
        print(player1.chips.bet)
        break

#-- Initial card dealings
card = deck.give_card()
card.is_face_up = True
player1.hand.add_card(card)
card = deck.give_card()
dealer.hand.add_card(card)
card = deck.give_card()
card.is_face_up = True
player1.hand.add_card(card)
card = deck.give_card()
card.is_face_up = True
dealer.hand.add_card(card)

print("{a} wagers: {b}".format(a=player1.nick,b=player1.chips.bet))
print('Player cards:')
dealcards = ''
for card in player1.hand.cards:
    dealcards += card.__str__()
print(dealcards)
print('Dealer cards:')
playercards = ''
for card in dealer.hand.cards:
    playercards += card.__str__()
print(playercards)

'''
while player1.turn:
    player1.make_bet()
    if player1.chips.bet > 0:
        player1.turn = False
        dealer.turn = True
'''

