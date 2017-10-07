# You need to create a simple text-based BlackJack game
# The game needs to have one player versus an automated dealer.
# The player can stand or hit.
# The player must be able to pick their betting amount.
# You need to keep track of the players total money.
# You need to alert the player of wins, losses, or busts, etc...

# Use classes to help you define the Deck and the Player's hand

from random import randint

cards = ('A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

class Player(object):

    def __init__(self, card, money):
        self.card = list()
        self.card.append(card)

        self.point = 0

        self.money = money
        print(self.card)


    def checkPoint(self):
        print(self.card)
        self.point = 0
        for c in self.card:
            if(c == 'J' or c== 'Q' or c=='K'):
                c = 10
            elif(c == 'A'):
                playerA = int(input("A be 1 or 11 "))   # try and except
                c = playerA
            else:
                c = int(c)

            self.point = self.point + c
        return self.point


    def stand(self):
        pass


    def hit(self):
        self.card.append(cards[randint(0, 13)])


    def remove(self):
        self.card = list()


class Dealer(object):

    def __init__(self, card):
        self.card = list()
        self.card.append(card)

        self.point = 0
        print(self.card)


    def checkPoint(self):
        print(self.card)
        self.point = 0
        for c in self.card:
            if(c == 'J' or c== 'Q' or c=='K'):
                c = 10
            elif(c == 'A'):
                if self.point < 10:
                    c = 11
                else:
                    c = 1
            else:
                c = int(c)

            self.point = self.point + c
            self.decision_making()


        return self.point

    def decision_making(self):
        if(self.point > 18):
            self.stand()
        else:
            self.hit()

    def stand(self):
        pass


    def hit(self):
        self.card.append(cards[randint(0, 13)])


    def remove(self):
        self.card = list()




player = Player(cards[randint(0, 13)], 100)

while True:
    try:
        player.remove()
        player.card.append(cards[randint(0, 13)])
        print("Money: ", player.money)
        # betting
        bet = int(input("Would much would you like to bet? "))
    except:
        print('Please enter a valid amount')
        continue
    else:
        if player.money >= bet:
            print('Your card: ' + player.card[0])

            while True:
                try:
                    # stand or hit
                    choose = int(input("Would you stand or hit?? Enter '1' to stand, '2' to hit "))
                except:
                    print('Please enter a valid number')
                    continue
                else:
                    if choose == 1:
                        player.stand()
                    elif choose == 2:
                        player.hit()

                        print(player.checkPoint())
                        if(player.checkPoint() > 21):
                            print("You fuck it up")
                            player.money = player.money - bet
                            break
                        else:
                            continue

                    else:
                        continue
                # finally:                  # need to cancel out the final

                    #playerPoint
                    print("Your Point now " ,player.checkPoint())

                    #dealer turn
                    print('dealer turn')
                    break



        else:
            print("You don't have enough money")
            continue

    finally:
        dealer = Dealer(cards[randint(0, 13)])
        dealer.checkPoint()
        print("Dealer deck ", dealer.card)
        print("Dealer point " ,dealer.point)

        if(dealer.point > 21):
            print("PLAYER WIN!!!!!!!!!!")
            player.money = player.money + bet

        if(21 >= dealer.point > player.point):
            print("DEALER WIN!!!!!!!!!!")
            player.money = player.money - bet
        elif(21 >= player.point > dealer.point):
            print("PLAYER WIN!!!!!!!!!!")
            player.money = player.money + bet

        #remove both player and dealer card
        player.remove()
        dealer.remove()
