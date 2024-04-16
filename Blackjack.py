from random import shuffle
from IPython.display import clear_output

class Blackjack:
    def __init__(self):
        self.deck = []
        self.suits = ("Spades", "Hearts", "Diamonds", "Clubs")
        self.values = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")

    def makeDeck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append((value, suit))
        shuffle(self.deck)

    def drawCard(self):
        return self.deck.pop()

class Player:
    def __init__(self, name, chips=100):
        self.name = name
        self.hand = []
        self.chips = chips
        self.bet = 0

    def addCard(self, card):
        self.hand.append(card)

    def showHand(self, dealer_start=True):
        print("\n{}".format(self.name))
        print("===========")
        for i, card in enumerate(self.hand):
            if self.name == "Dealer" and i == 0 and dealer_start:
                print("- of –")  # Hide first card
            else:
                print("{} of {}".format(card[0], card[1]))
        if self.name != "Dealer" or not dealer_start:
            print("Total = {}".format(self.calcHand(dealer_start)))

    def calcHand(self, dealer_start=True):
        total = 0
        aces = 0
        card_values = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "J": 10, "Q": 10, "K": 10, "A": 11}
        if self.name == "Dealer" and dealer_start:
            card = self.hand[1]
            return card_values[card[0]]
        for card in self.hand:
            if card[0] == "A":
                aces += 1
            else:
                total += card_values[card[0]]
        for _ in range(aces):
            if total + 11 > 21:
                total += 1
            else:
                total += 11
        return total

    def placeBet(self):
        while True:
            try:
                bet = int(input("How much would you like to bet? (Current chips: {}): ".format(self.chips)))
                if bet > self.chips or bet <= 0:
                    print("Invalid bet amount. Please try again.")
                else:
                    self.bet = bet
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def winBet(self):
        self.chips += self.bet

    def loseBet(self):
        self.chips -= self.bet

    def tieBet(self):
        self.chips += self.bet

# Main game loop
def blackjack_game():
    # Initialize game
    game = Blackjack()
    game.makeDeck()

    # Create player and dealer
    player_name = input("What is your name? ")
    player = Player(player_name)
    dealer = Player("Dealer")

    # Place initial bets
    player.placeBet()

    # Deal initial cards
    for _ in range(2):
        player.addCard(game.drawCard())
        dealer.addCard(game.drawCard())

    # Show initial hands
    clear_output()
    player.showHand()
    dealer.showHand()

    # Player's turn
    while input("Would you like to stay or hit? (stay/hit) ").lower() != "stay":
        clear_output()
        player.addCard(game.drawCard())
        player.showHand()
        dealer.showHand()

        if player.calcHand() > 21:
            print("Busted! You lose.")
            player.loseBet()
            return

    # Dealer's turn
    clear_output()
    dealer.showHand(False)
    while dealer.calcHand(False) < 17:
        dealer.addCard(game.drawCard())
        dealer.showHand(False)

    # Determine winner
    player_total = player.calcHand()
    dealer_total = dealer.calcHand(False)
    if player_total > dealer_total or dealer_total > 21:
        print("Congratulations! You win!")
        player.winBet()
    elif player_total < dealer_total:
        print("Dealer wins. You lose.")
        player.loseBet()
    else:
        print("It's a tie!")

    print("Remaining chips: {}".format(player.chips))

    # Ask to play again
    play_again = input("Would you like to play again? (yes/no) ").lower()
    if play_again == "yes":
        blackjack_game()
    else:
        print("Thanks for playing!")

# Start the game
blackjack_game()
