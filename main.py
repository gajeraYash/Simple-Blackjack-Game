import func as f
import classdef as c
f.info()
userChips = c.Chips(f.buyin())

while True:
    deck = c.Deck()
    deck.shuffle()

    userHand = c.Hand()
    userHand.add_card(deck.deal())
    userHand.add_card(deck.deal())

    dealerHand = c.Hand()
    dealerHand.add_card(deck.deal())
    dealerHand.add_card(deck.deal())

    f.take_bet(userChips)

    f.show_init(userHand,dealerHand)
    while f.playing:  
        f.hit_or_stand(deck,userHand)
        f.show_init(userHand,dealerHand)
        if userHand.value > 21:
            f.player_busts(userChips)
            break
    if userHand.value <= 21:
        while dealerHand.value <17:
            f.hit(deck,dealerHand)
        f.show_all(userHand,dealerHand)

        #Different Scenarios
        if dealerHand.value > 21:
            f.dealer_busts(userChips)
        elif dealerHand.value > userHand.value:
            f.dealer_wins(userChips)
        elif dealerHand.value < userHand.value:
            f.player_wins(userChips)
        else:
            f.push()
        
    print("\nTotal Chips: ",userChips.total)
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        f.playing = True
        f.reset()
        print("\nTotal Chips: ",userChips.total)
        continue
    else:
        print("Thanks for playing!")
        break