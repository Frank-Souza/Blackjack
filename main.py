import random

class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        self.cards = [(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Player:
    def __init__(self):
        self.hand = []

    def draw(self, deck, numberOfCards):
        for i in range(numberOfCards):
            card = deck.deal()
            self.hand.append(card)
    
    def handValue(self, deck):
        value = 0
        for card in deck:
            rank = card[0]
            if rank in ['2', '3', '4', '5', '6', '7', '8', '9']:
                value += int(rank)
            elif rank in ['10', 'J', 'Q', 'K']:
                value += 10
            elif rank == 'A':
                value += 11
        return value

class Game:
    def __init__(self) -> None:
        pass

    def play(self, value, hand, player, deck, dealer):
        if value == 21:
            print('Blackjack!')
            bust = False
            return value, hand, bust
        elif dealer == 21:
            print('Dealer blackjack')
            bust = False
            return value, hand, bust
        choice = input(f'Here is your hand: {hand} Hit or Stand?\n')
        bust = False
        if choice == 'stand':
            return value, hand, bust
        while choice == 'hit' and value < 21:
            player.draw(deck, 1)
            hand = player.hand
            value = player.handValue(player.hand)
            if value < 21:
                choice = input(f'Here is your hand: {hand} Hit or Stand?\n')
            else:
                pass
        if value > 21:
            bust = True
        print(f'Player hand: {value, hand}')
        return value, hand, bust

    def dealerPlay(self, value, hand, dealer, deck):
        bust = False
        if value == 21:
            print(hand)
            bust = False
            return value, hand, bust
        while value < 17:
            dealer.draw(deck, 1)
            value = dealer.handValue(dealer.hand)
        if value > 21:
            bust = True
        print (f'Dealer hand: {value, hand}')
        return value, hand, bust

    def findWinner(self, pbust, dbust, pvalue, dvalue):
        if pbust == True:
            print ('Dealer wins')
        elif dbust == True:
            print ('Player wins')
        elif pvalue > dvalue:
            print ('Player wins')
        elif dvalue > pvalue:
            print ("Dealer wins")
        elif dvalue == pvalue:
            print ("Push")
        else:
            print ('How did we end up here')

    def initializeGame(self):
        deck = Deck()
        deck.shuffle()
        player = Player()
        dealer = Player()
        player.draw(deck, 2)
        dealer.draw(deck, 2)
        playerScore = player.handValue(player.hand)
        dealerScore = dealer.handValue(dealer.hand)

        game = Game()
        print(f'player = {playerScore} dealer = {dealerScore}')

        player_score, player_hand, player_bust = game.play(playerScore, player.hand, player, deck, dealerScore)
        dealer_score, dealer_hand, dealer_bust = game.dealerPlay(dealerScore, dealer.hand, dealer, deck)
        game.findWinner(player_bust, dealer_bust, player_score, dealer_score)
        choice = input(f'Want to play again?(y/n)\n')
        while choice != 'n' and choice != 'y':
            print('Please enter y or n')
            choice = input(f'Want to play again?(y/n)\n')
        if choice == 'n':
            print('Hope you had fun!')
        elif choice == 'y':
            Game().initializeGame()

print(len(Deck().cards))
Game().initializeGame()






