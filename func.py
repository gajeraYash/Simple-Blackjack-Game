from os import system
playing = True

def info():
    print("\t\t Simple Blackjack Game \t\t\n\t\tCreated By Yash Gajera\n")

def buyin():
    print("Specify the amount of chips you would like to buy-in.")
    while True:
        try:
            amount = int(input("Amount of Chips: "))
        except ValueError:
            print("Input should be a integer value.")
        else:
            if amount > 10000:
                print("MAX AMOUNT: 10,000")
            else:
                return amount
        
def take_bet(chips):
    if chips.total < 100:
        print("You dont have enough chips to bet!")
        chips.total = buyin()
    else:
        while True:
            try:
                chips.bet = int(input('Bet: '))
            except ValueError:
                print("Input should be a integer value.")
            else:
                if chips.bet > chips.total:
                    print("Bet exceeds total chips!\nTotal Chips: ",chips.total)
                elif chips.bet < 100:
                    print("Minimum bet is 100")
                else:
                    break

        
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        x = input("\nWould you like to Hit or Stand? Enter 'h' or 's': ")
    
        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
            print(playing)

        else:
            print("Sorry, please try again.")
            continue
        break
    print(playing)

def show_init(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    pass
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    pass

def player_busts(chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push():
    print("Dealer and Player tie! It's a push.")

def reset():
    system('clear')
    info()
    
