import os
import random
from colorama import init, Fore, Back, Style
init(autoreset=True)  # Set auto reset to ensure each line resets color

player_dict = {}



class Deck():
    def __init__(self):
        self.cards = 6*["king"] + 6*["queen"] + 6*["ace"] + 2*["joker"]

    def shuffle_deck(self):
        random.shuffle(self.cards)

        
# a simple Player class with some properties
class Player():
    def __init__(self, name, cards):
        self.pistol = [0, 0, 0, 0, 0, 0]
        self.name = name
        self.cards = cards
        self.pistol[random.randint(0, 5)] = 1


def get_valid_integer(prompt, min, max):
    while True:
        try:
            value = int(input(prompt))
            if (value is not None and value < min) or (value is not None and value > max):
                print("please enter a valid number: -> ")
                continue
            return value
        except ValueError:
            print("please enter a number: -> ")


def get_y_or_n():
    while True:
        value = input("Ask for a liar? say 'y' or 'n'-> ").strip().lower()
        if value in ['y', 'n']:
            return value
        print("Please enter valid response('y' or 'n') -> ")
        

def get_valid_card_name(current_card_list):
    while True:
        card = input("Which card you want to put:-> ").strip().lower()
        if card in current_card_list:
            return card
        print("Please enter valid card from your deck please check :-> ", current_card_list)


def print_rule():
    return 'rules:>'


def random_game_table():
    game_table_content = ["king", "queen", "ace"]
    game_table = random.choice(game_table_content)
    return game_table


def initiate_player(number_of_players):
    number_of_cards_to_play = 5
    cards1 = Deck()
    cards1.shuffle_deck()
    for i in range(number_of_players):
        while True:
            name = input("Enter your name-> ").strip().lower()
            if name not in list(player_dict.keys()):
                player_dict[name] = Player(name, cards1.cards[i*number_of_cards_to_play:(i*number_of_cards_to_play)+number_of_cards_to_play])
                break
            print("The name is already taken!! Please add a new Name-> ")
    return player_dict


def card_allotment():
    number_of_cards_to_play = 5
    cards1 = Deck()
    cards1.shuffle_deck()
    for i in range(len(shuffled_player_list)):
        player_dict[shuffled_player_list[i]].cards = cards1.cards[i*number_of_cards_to_play:(i*number_of_cards_to_play)+number_of_cards_to_play]
    return 


def shuffle_player(player_dict):
    shuffled_player_list = list(player_dict.keys())
    random.shuffle(shuffled_player_list)
    return shuffled_player_list


def eliminate(player_name):
    shuffled_player_list.remove(player_name)
    # if len(shuffled_player_list) < 2:
    #     print(f"Contratulations!!!!! {shuffled_player_list[0]} is the winner...Hurrrayyyyy")


# a function that'll do what it says
def fire_pistol(player_name):
    print(f" ### The pistol has been fired by {player_name} ###")

    if player_list[player_name].pistol[0] == 1:
        print(f" !!! Sorry {player_name} is dead. !!! ")
        return eliminate(player_name)
    else:
        print(f" ### But {player_name} is safe [ 'for now :)' ] ###")
        del player_list[player_name].pistol[0]
    print(shuffled_player_list)
    card_allotment()

    main_game_logic()

# player name input random pistol and random cards
player_list = (initiate_player(get_valid_integer("Enter number of players-> ", 2, 4)))
shuffled_player_list = shuffle_player(player_list)


# game logic
# cards_queue = []
# count = 0
# game_over = False
# game_table = random_game_table()
# previous_player = ''


def main_game_logic():
    print("\n New game started")
    cards_queue = []
    count = 0
    game_over = False
    game_table = random_game_table()
    previous_player = ''


    while True:

        # # check if there is only one player remaining
        # if len(shuffled_player_list) < 2:
        #     print(Fore.GREEN+"Contratulations!!!!! " + shuffled_player_list[0]+ " is the winner...Hurrrayyyyy")
        #     break

        # a loop that'll be alsways running until someone wins
        for player_turn in shuffled_player_list:
            print(Fore.YELLOW + "game table:- " + game_table)
            print(Fore.YELLOW +  "Player Turn:- " + player_turn)
            print(Fore.MAGENTA + f'{player_turn}:- {player_list[player_turn].cards}')

            # checking for the game's first play (so that he can't see the option to say Liar to his/her previous player)
            if count != 0:
                ask_for_lie = get_y_or_n()
                if ask_for_lie == "n":
                    pass
                else:
                    # if someone decides to say "Liar"2
                    # make a new list only for last player's cards
                    cards_to_check = cards_queue[-(player_choice_number):]

                    # Check for jocker if yes then add same as game table in cards_to_check
                    cards_to_check = [card for card in cards_to_check if card != 'joker']
                    print(cards_to_check)

                    # check if cards are right as game table or not
                    if (len(set(cards_to_check)) == 1 and cards_to_check[0] == game_table) or len(cards_to_check) == 0:
                        # current person has to fire pistol
                        fire_pistol(player_turn)

                    else:
                        # previous person has to fire pistol
                        fire_pistol(previous_player)
                    
            # check if there is only one player remaining
            if len(shuffled_player_list) < 2:
                print(shuffled_player_list)
                print(Fore.GREEN+"Contratulations!!!!! " + shuffled_player_list[0]+ " is the winner...Hurrrayyyyy")
                return



            # the number of cards player wants to draw
            player_choice_number = get_valid_integer("Enter number of cards you want to Draw(1 to 3)-> ", 1, 3)

            # selection cards and then adding it to card queue that is placed in the middle of all players
            for card in range(player_choice_number):
                player_choice_card = get_valid_card_name(player_list[player_turn].cards)
                cards_queue.append(player_choice_card)
                player_list[player_turn].cards.remove(player_choice_card)
                count = count + 1
            previous_player = player_turn
            os.system('cls' if os.name == 'nt' else 'clear')


main_game_logic()