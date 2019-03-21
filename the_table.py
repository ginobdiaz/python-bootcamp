import time
import uuid
from Blackjack import deckengine as de

'''
'''

def show_cards(player,dealer):
    print('\n'*100)
    playercards = ''
    for card in player.hand.cards:
        playercards += card.__str__()
    print('_'*40)        
    print(playercards)
    print('_'*40)
    print("| {a} bets {b} {c}".format(a=player.nick,b=player.chips.bet,c=player.status))
    print('_'*40)
    
    print(' ')
    dealcards = ''   
    for card in dealer.hand.cards:
        dealcards += card.__str__()
    print('_'*40)
    print(dealcards)
    print('_'*40)
    print('| Dealer {a} '.format(a=dealer.status))
    print('_'*40)

def show_round_results(player, dealer):
    if ("BUSTED" in player.status and "BUSTED" not in dealer.status) or dealer.valid_score > player.valid_score:
        dealer.status += " **WINNER**"
        player.chips.lose_bet()
    elif "BUSTED" not in player.status and "BUSTED" in dealer.status or player.valid_score > dealer.valid_score:
        player.status += " **WINNER**"
        player.chips.win_bet()
    elif player.valid_score == dealer.valid_score:
        player.status += " **A PUSH**"
        dealer.status += " **A PUSH**"

    player.status += " Total chips:" + str(player.chips.total)
    show_cards(player, dealer)


deck = de.Deck()
#for card in deck.cards:
#    print(card)
player1 = de.Player('Cindo',bankroll=200)
dealer = de.Dealer()
deck.shuffle()
player1.turn = True
print('\n'*100)

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
player1.set_status()
dealer.set_status()

show_cards(player1, dealer)
'''
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
    if player1.hit_or_stand():
        player1.hit(deck.give_card())
        
    dealer.turn = True if not player1.turn else False
    show_cards(player1,dealer)
    if dealer.turn:
        break
#    print('dealer')
#    print(dealer.turn )
#    print('player')
#    print(player1.turn )
    #quit()


while True: #dealer.turn:
    if dealer.hand.score < 17:
        dealer.hit(deck.give_card())
    else:
        dealer.set_status()
    #player1.turn = True if not dealer.turn else False

    dealer.hand.show_all()   
    show_cards(player1,dealer)
    time.sleep(3)

    if not dealer.turn:
        break

show_round_results(player1, dealer)

 #   if player1.chips.bet > 0:
 #       player1.turn = False
 #       dealer.turn = True


