import random
import time as tm

player_avail_points = 20
program_is_open = True
isRunning = True
player_cards = 0
dealer_cards = 0

def player_card_draw():
    global player_cards
    card = random.randint(2, 10)
    print(f"Your card is a...{card}")
    player_cards += card
   
def dealer_card_draw():
    global dealer_cards
    card = random.randint(2, 10)
    print(f"The dealers card is a...{card}")
    dealer_cards += card
    
def hit_me(value):
    if value == 'player':
        player_card_draw()
    elif value =='dealer':
        dealer_card_draw()

def place_bet(player_points):
    bet = input(f'Place your bet! You have {str(player_points)} points\n')
    num_bet = int(bet)
    if num_bet > player_points:
        num_bet == player_points
    return num_bet

def prompt_user():
    res = input('[1] Hit Me \n[2] Stand \n')
    return res

def winner(winning_player, points_what_todo):
    global player_avail_points
    if winning_player == 'User':
        player_avail_points += points_what_todo
    elif winning_player == 'Dealer':
        player_avail_points -= points_what_todo

def check_bust(value):
    global isRunning

    if value >= 22 :
        isRunning = False
        if value == player_cards:
            print("Player Bust! Try again")
        elif value == dealer_cards:
            print("Dealer Bust! Nice Win")

def main_game():
    global isRunning, player_cards, dealer_cards, player_avail_points

    print('*** Welcome to 21! Your goal is to get as close to 21 without going over. You will start with two "Cards" between 2 and 10 ***')
    placed_bet = place_bet(player_avail_points)

    player_card_draw()
    player_card_draw()
    dealer_card_draw()

    while(isRunning):
        print(f"\nYour card total: {player_cards} \nDealer card total: {dealer_cards}")
        x = prompt_user()
        if x == '1' and player_cards <= 22:
            player_card_draw()
            check_bust(player_cards)
        if x == '2': 
            while(dealer_cards <= 16):
                dealer_card_draw()
                print(f"\nYour card total: {player_cards} \nDealer card total: {dealer_cards}")
                check_bust(dealer_cards)
                tm.sleep(1.5)
        
            if dealer_cards >= 17 and dealer_cards <= 21:
                isRunning = False

    if isRunning == False and player_cards <= 21 and dealer_cards <= 21:
        if player_cards > dealer_cards:
            print('You win!')
            winner('User', placed_bet)

        elif player_cards < dealer_cards:
            print('Dealer Wins!')
            winner('Dealer', placed_bet)
        else:
            print('Tie!')

def prompt_play_game():
    global player_cards, dealer_cards, program_is_open, isRunning, player_avail_points
    ready_to_play = input('Ready to play!\n[1]Yes\n[2]No\n')
    if ready_to_play == '1':
        player_cards = 0
        dealer_cards = 0
        isRunning = True
        main_game()
    elif ready_to_play =='2':
        program_is_open = False


while(program_is_open):
    prompt_play_game()








