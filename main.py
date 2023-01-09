import random
import math

class cards:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

# Deck
two = cards("Two", 2)
three = cards("Three", 3)
four = cards("Four", 4)
five = cards("Five", 5)
six = cards("Six", 6)
seven = cards("Seven", 7)
eight = cards("Eight", 8)
nine = cards("Nine", 9)
ten = cards("Ten", 10)
jack = cards("Jack", 10)
queen = cards("Queen", 10)
king = cards("King", 10)
ace = cards("Ace", 11)

deck = [two.amount, three.amount, four.amount, five.amount, six.amount, seven.amount, eight.amount, nine.amount, ten.amount, jack.amount, queen.amount, king.amount, ace.amount]
deal = [random.sample(deck, 2), random.sample(deck, 2)]
p1 = player("Frank", deal[0])
p2 = player("Dealer", deal[1])

def dealerStart():
    print (f'Dealer total is: {sum(p2.hand)}')

def game():
    print (f'Here is your current hand: \nTotal = {sum(p1.hand)}')
    i = sum(p1.hand)
    while True:
        if i == 21:
            print('Hand total is 21')
            break
        elif i > 21:
            print ('Bust')
            break
        elif input("Hit or Stand?\n") == "hit":
            p1.hand += (random.sample(deck, 1))
            i = sum(p1.hand)
            print (f'Hand total is now: {sum(p1.hand)}')
        else:
            break

def dealerGame():
    print("Dealer game starts:")
    if sum(p2.hand) < 17:
        p2.hand += (random.sample(deck, 1))
        print(f'Dealers hand is now {sum(p2.hand)}')
        if sum(p2.hand) < 17:
            p2.hand += (random.sample(deck, 1))
            print(f'Dealers hand is now {sum(p2.hand)}')
            if sum(p2.hand) < 17:
                p2.hand += (random.sample(deck, 1))
                print(f'Dealers hand is now {sum(p2.hand)}')
    elif sum(p2.hand) >= 17 and sum(p2.hand) <= 21:
        print (f'Dealers hand is {sum(p2.hand)}')
    else:
        print (f'Dealer bust with a hand of {sum(p2.hand)}')

def findTheWinner():
    if sum(p1.hand) > 21:
        print ("Dealer wins")
    elif sum(p2.hand) > 21:
        print ("Player wins")
    elif sum(p1.hand) == sum(p2.hand):
        print("Push")
    elif sum(p1.hand) > sum(p2.hand):
        print ("Player wins")
    elif sum(p1.hand) < sum(p2.hand):
        print ("Dealer wins")

def resetHands():
    global p1
    global p2
    global deal
    deal = [random.sample(deck, 2), random.sample(deck, 2)]
    p1 = player("Frank", deal[0])
    p2 = player("Dealer", deal[1])

def playAgain():
    if input("Type yes if you would like to play again\n") == "yes":
        dealerStart()
        game()
        dealerGame() 
        findTheWinner()
        resetHands()
        playAgain()
    else:
        print("hope you had fun!")

dealerStart()
game()
dealerGame() 
findTheWinner()
resetHands()
playAgain()






