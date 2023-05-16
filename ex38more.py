"""
Go Fish Game - by ChatGPT
"""

from collections import Counter
import random

# # Define card suits and ranks
# suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
# ranks = ['Ace', '2', '3', '4', '5', '6', '7',
#          '8', '9', '10', 'Jack', 'Queen', 'King']

# # Create a deck of cards
# deck = [(rank, suit) for rank in ranks for suit in suits]

# # Shuffle the deck
# random.shuffle(deck)

# # Deal the cards
# player_hand = []
# computer_hand = []
# for i in range(7):
#     player_hand.append(deck.pop())
#     computer_hand.append(deck.pop())

# # Play the game
# while True:
#     # Display player's hand
#     print("Your hand: ", player_hand)

#     # Ask for a card
#     card_rank = input("Ask for a card: ")

#     # Check if card is in computer's hand
#     if card_rank in [card[0] for card in computer_hand]:
#         # Remove card from computer's hand and add to player's hand
#         for i, card in enumerate(computer_hand):
#             if card[0] == card_rank:
#                 player_hand.append(card)
#                 del computer_hand[i]
#                 print("Computer gave you the", card_rank)
#                 break
#     else:
#         # Draw a card from the deck
#         if len(deck) > 0:
#             drawn_card = deck.pop()
#             player_hand.append(drawn_card)
#             print("Go fish! You drew the", drawn_card[0])
#         else:
#             # Game over if deck is empty
#             print("Deck is empty! Game over.")
#             break

#     # Check for book in player's hand
#     book_ranks = [rank for rank in ranks if [
#         card for card in player_hand if card[0] == rank]]
#     for rank in book_ranks:
#         # Remove cards from player's hand and add to pile
#         pile = [card for card in player_hand if card[0] == rank]
#         player_hand = [card for card in player_hand if card[0] != rank]
#         print("You got a book of", rank)

#     # Check for book in computer's hand
#     book_ranks = [rank for rank in ranks if [
#         card for card in computer_hand if card[0] == rank]]
#     for rank in book_ranks:
#         # Remove cards from computer's hand and add to pile
#         pile = [card for card in computer_hand if card[0] == rank]
#         computer_hand = [card for card in computer_hand if card[0] != rank]
#         print("Computer got a book of", rank)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.book = []
        self.score = 0

    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self, card):
        self.hand.remove(card)

    # def check_book(self):
    #     for card in set(self.hand):
    #         if self.hand.count(card) == 4:
    #             self.book.append(card)
    #             self.score += 1
    #             for i in range(4):
    #                 self.hand.remove(card)

    def check_book(self):
        """
        Check if the player has any book, and if so, remove those cards from their hand
        and add the book to their book list. Returns the number of books found.
        """
        book_count = 0
        ranks_in_hand = [card[0] for card in self.hand]
        hand_counter = Counter(ranks_in_hand)
        for rank_in_hand, count in hand_counter.items():
            if count == 4:
                self.hand = [c for c in self.hand if c[0] != rank_in_hand]
                self.book.append(rank_in_hand)
                book_count += 1
        # TODO: update score
        return book_count

    def draw_card(self, deck):
        card = deck.pop()
        self.add_card(card)
        self.check_book()

    def has_card(self, rank):
        return rank in [card[0] for card in self.hand]

    def ask_card(self, rank, other_player):
        if other_player.has_card(rank):
            for card in other_player.hand:
                if card[0] == rank:
                    self.add_card(card)
                    other_player.remove_card(card)
            self.check_book()
            return True
        return False

    def show_hand(self):
        print(f"{self.name}'s hand: {' '.join(self.hand)}")

    def show_books(self):
        print(f"{self.name}'s books: {' '.join(self.book)}")


class GoFish:
    def __init__(self, players):
        self.players = players
        self.current_player_index = 0
        self.deck = []

    def prepare_deck(self):
        ranks = [str(num) for num in range(2, 11)] + ['J', 'Q', 'K', 'A']
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.deck = [(rank, suit) for rank in ranks for suit in suits]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_cards(self):
        for i in range(5):
            for player in self.players:
                player.draw_card(self.deck)

    def get_current_player(self):
        return self.players[self.current_player_index]

    def next_turn(self):
        self.current_player_index = (
            self.current_player_index + 1) % len(self.players)

    def play_round(self):
        current_player = self.get_current_player()
        print(f"Current player: {current_player.name}")
        current_player.show_hand()
        current_player.show_books()
        rank = input("Choose a rank to ask for: ")
        other_player_index = int(
            input(f"Choose a player (1-{len(self.players)}) to ask: ")) - 1
        other_player = self.players[other_player_index]
        if current_player.ask_card(rank, other_player):
            print("Good guess! You get to go again.")
        else:
            print("Go fish!")
            current_player.draw_card(self.deck)
            self.next_turn()

    def play_game(self):
        self.prepare_deck()
        self.shuffle_deck()
        self.deal_cards()
        while True:
            self.play_round()
            for player in self.players:
                player.show_books()
            if len(self.deck) == 0 and all(len(player.hand) == 0 for player in self.players):
                break
        print("Game over!")
        for player in self.players:
            print(f"{player.name}'s score: {player.score}")
