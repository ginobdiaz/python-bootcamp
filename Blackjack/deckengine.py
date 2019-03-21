import uuid
import random

class Suit:
    def __init__(self,name,color,shape,abbr):
        self.name = name
        self.color = color
        self.shape = shape
        self.abbr = abbr
    
    def __str__(self):
        return self.name.capitalize()

class Face:
    def __init__(self,name,abbr,rank):
        self.name = name
        self.abbr = abbr
        self.rank = rank
        self.alt_rank = rank

class Card:
    def __init__(self,id,Suit,Face):
        self.id = id
        self.suit = Suit
        self.face = Face
        self.is_face_up = False

    def __str__(self):
        if self.is_face_up:
            return "[ %s%s ]" %(self.face.abbr, self.suit.abbr)
        else:
            return "[ ?? ]"

class Deck:

    # Joker is a placeholder and should never happen
    joker = Suit(name='joker',color='white',shape='humanoid',abbr='w')
    joke_face = Face(name='Joker',abbr='LOL',rank=-1)
    joke_card = Card(id=str(uuid.uuid4()),Suit=joker,Face=joke_face)
    del joke_face

    def __init__(self):
        # Suits
        heart = Suit(name='heart',color='red',shape='round',abbr='h')
        diamond = Suit(name='diamond',color='red',shape='pointy',abbr='d')
        club = Suit(name='club',color='black',shape='round',abbr='c')
        spade = Suit(name='spade',color='black',shape='pointy',abbr='s')

        #create the deck
        self.cards = []
        ## The Hearts
        face = Face(name='Ace',abbr='A',rank=1)
        face.alt_rank = 11
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=heart,Face=face))
        del face
        face = Face(name='Two',abbr='2',rank=2)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=heart,Face=face))
        face = Face(name='Three',abbr='3',rank=3)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=heart,Face=face))
        face = Face(name='Four',abbr='4',rank=4)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=heart,Face=face))
        face = Face(name='Five',abbr='5',rank=5)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=heart,Face=face))
        face = Face(name='Six',abbr='6',rank=6)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=heart,Face=face))
        face = Face(name='Seven',abbr='7',rank=7)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=heart,Face=face))
        face = Face(name='Eight',abbr='8',rank=8)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=heart,Face=face))
        face = Face(name='Nine',abbr='9',rank=9)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=heart,Face=face))
        face = Face(name='Ten',abbr='T',rank=10)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=heart,Face=face))
        face = Face(name='Jack',abbr='J',rank=10)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=heart,Face=face))
        face = Face(name='Queen',abbr='Q',rank=10)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=heart,Face=face))
        face = Face(name='King',abbr='K',rank=10)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=heart,Face=face))

        ## The Diamonds
        face = Face(name='Ace',abbr='A',rank=1)
        face.alt_rank = 11
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=diamond,Face=face))
        del face
        face = Face(name='Two',abbr='2',rank=2)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=diamond,Face=face))
        face = Face(name='Three',abbr='3',rank=3)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=diamond,Face=face))
        face = Face(name='Four',abbr='4',rank=4)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=diamond,Face=face))
        face = Face(name='Five',abbr='5',rank=5)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=diamond,Face=face))
        face = Face(name='Six',abbr='6',rank=6)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=diamond,Face=face))
        face = Face(name='Seven',abbr='7',rank=7)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=diamond,Face=face))
        face = Face(name='Eight',abbr='8',rank=8)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=diamond,Face=face))
        face = Face(name='Nine',abbr='9',rank=9)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=diamond,Face=face))
        face = Face(name='Ten',abbr='T',rank=10)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=diamond,Face=face))
        face = Face(name='Jack',abbr='J',rank=10)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=diamond,Face=face))
        face = Face(name='Queen',abbr='Q',rank=10)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=diamond,Face=face))
        face = Face(name='King',abbr='K',rank=10)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=diamond,Face=face))

        ## The Clubs
        face = Face(name='Ace',abbr='A',rank=1)
        face.alt_rank = 11
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=club,Face=face))
        del face
        face = Face(name='Two',abbr='2',rank=2)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=club,Face=face))
        face = Face(name='Three',abbr='3',rank=3)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=club,Face=face))
        face = Face(name='Four',abbr='4',rank=4)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=club,Face=face))
        face = Face(name='Five',abbr='5',rank=5)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=club,Face=face))
        face = Face(name='Six',abbr='6',rank=6)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=club,Face=face))
        face = Face(name='Seven',abbr='7',rank=7)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=club,Face=face))
        face = Face(name='Eight',abbr='8',rank=8)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=club,Face=face))
        face = Face(name='Nine',abbr='9',rank=9)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=club,Face=face))
        face = Face(name='Ten',abbr='T',rank=10)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=club,Face=face))
        face = Face(name='Jack',abbr='J',rank=10)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=club,Face=face))
        face = Face(name='Queen',abbr='Q',rank=10)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=club,Face=face))
        face = Face(name='King',abbr='K',rank=10)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=club,Face=face))

        ## The Spades
        face = Face(name='Ace',abbr='A',rank=1)
        face.alt_rank = 11
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=spade,Face=face))
        del face
        face = Face(name='Two',abbr='2',rank=2)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=spade,Face=face))
        face = Face(name='Three',abbr='3',rank=3)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=spade,Face=face))
        face = Face(name='Four',abbr='4',rank=4)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=spade,Face=face))
        face = Face(name='Five',abbr='5',rank=5)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=spade,Face=face))
        face = Face(name='Six',abbr='6',rank=6)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=spade,Face=face))
        face = Face(name='Seven',abbr='7',rank=7)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=spade,Face=face))
        face = Face(name='Eight',abbr='8',rank=8)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=spade,Face=face))
        face = Face(name='Nine',abbr='9',rank=9)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=spade,Face=face))
        face = Face(name='Ten',abbr='T',rank=10)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=spade,Face=face))
        face = Face(name='Jack',abbr='J',rank=10)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=spade,Face=face))
        face = Face(name='Queen',abbr='Q',rank=10)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=spade,Face=face))
        face = Face(name='King',abbr='K',rank=10)
        self.cards.append(Card(id=str(uuid.uuid4()),Suit=spade,Face=face))

        self.heart = heart
        self.diamond = diamond
        self.club = club
        self.spade = spade

    def shuffle(self):
        random.shuffle(self.cards)

    def give_card(self):
        if len(self.cards) == 0:
            return Deck.joke_card
        else:
            return self.cards.pop(0)

class Hand:
    def __init__(self):
        self.cards = []
        self.score = 0
        self.alt_score = 0

    def add_card(self,card):
            self.score += card.face.rank
            self.alt_score += card.face.alt_rank
            self.cards.append(card)

    def rescore(self):
        for card in self.cards:
            self.score += card.face.rank
            self.alt_score += card.face.alt_rank

    def show_all(self):
        for card in self.cards:
            card.is_face_up = True
    
    def has_face_downs(self):
        for card in self.cards:
            if not card.is_face_up:
                return True

        return False



class Chips:
    number_wins = 0
    number_loses = 0

    def __init__(self,total=0):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
        Chips.number_wins += 1

    def lose_bet(self):
        self.total -= self.bet
        Chips.number_loses += 1

    def set_bet(self, bet=0):
        if bet > self.total:
            print ("You cannot bet more than you have. Bet:%s Your Total:%s" %(bet, self.total))
            return False
        
        self.bet = bet
        return True
    
class HouseChips(Chips):
    def __init__(self,bankroll=10000):
        Chips.__init__(self,bankroll)



class Player:

    def __init__(self,nick='',bankroll=0):
        self.nick = nick
        self.turn = False
        self.chips = Chips(bankroll)
        self.hand = Hand()
        self.status = ''

    def make_bet(self):
        try:
            if self.turn:
                bet=int(input('Please, make your wager: '))
                if self.chips.set_bet(bet):
                    print("{a} bet is {b}".format(a=self.nick,b=self.chips.bet))
            else:
                print('Sorry not your turn.')
        except:
            print('Sorry you must place a numberic bet.')
            self.chips.bet = 0

    def hit_or_stand(self):
        try:
            ans = input('Hit or Stand (H/S): ')
            if ans[0].upper() == 'H':
                return True
            elif ans[0].upper() == 'S':
                self.turn = False

        except:
            print('Please only enter an H or an S')
        
        return False

    def hit(self,card):
        card.is_face_up = True
        self.hand.add_card(card)
        self.set_status()   
    
    def set_status(self):
        if self.hand.score > 21:
            self.status = 'has BUSTED with ' + str(self.hand.score)
            self.turn = False
        elif self.hand.score == 21 or self.hand.alt_score == 21:
            self.status = 'hit 21!'
            self.turn = False
        else:
            if self.hand.score != self.hand.alt_score:
                self.status = 'has ' + str(self.hand.alt_score) + ' or ' + str(self.hand.score)
            else:
                self.status = 'has ' + str(self.hand.score)

class Dealer(Player):

    def __init__(self):
        Player.__init__(self,nick='Dealer',bankroll=10000)


    def make_bet(self):
        print("Dealers cannot make bets.")

    def set_status(self):
        if self.hand.score > 21:
            self.status = 'has BUSTED with ' + str(self.hand.score)
            self.turn = False
        elif self.hand.score == 21 or self.hand.alt_score == 21:
            self.status = 'hit 21!'
            self.turn = False
        else:
            if not self.hand.has_face_downs():
                if self.hand.score != self.hand.alt_score:
                    self.status = 'has ' + str(self.hand.alt_score) + ' or ' + str(self.hand.score)
                else:
                    self.status = 'has ' + str(self.hand.score)

