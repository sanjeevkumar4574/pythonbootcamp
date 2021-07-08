import  random
from art import logo3
def play_game():
    print(logo3)
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    def cal_score(cards):
        """takes cards and calculated score from cards, return """
        if sum(cards)==21 and len(cards)==2:
            return 0
        if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)
    def compare(user,computer):
        if user==computer:
            return 'draw'
        elif user==0:
            return 'you win'
        elif computer==0:
            return 'you worst'
        elif user>21:
            return 'you went over . you lose'
        elif computer>21:
            return 'opponent went over . you win'
        elif user>computer:
            return 'you win'
        else:
            return 'you lose'

    is_game_over = False
    while is_game_over==False:
        user_score=cal_score(user_cards)
        computer_score=cal_score(computer_cards)
        print(f"you cards: {user_cards} and current score {user_score}")
        print(f"computer first card: {computer_cards[0]} ")
        if user_score==0 or computer_score==0:
            is_game_over = True
        else:
            th_iteam = input("type 'y' if you want to hit or 'n' if you don't want to hit. ")
            if th_iteam =='y':
                user_cards.append(deal_card())
                print(f"you cards: {user_cards} and current score {user_score+deal_card()}")

            else:
                is_game_over = True
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score = cal_score(computer_cards)
    print(f"your final score: {user_cards}, {user_score}")
    print(f"compter final score: {computer_cards}, {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want play blackjack game type 'y' otherwise 'n' ") == 'y':
    play_game()

# if user_score>computer_score and user_score<21:
#     print(f"you won {user_score}.")
# elif user_score<computer_cards and computer_score<21:
#     print(f"computer won {user_score}" )
# elif user_score==computer_score and computer_score<21:
#     print(f"game draw {computer_score}")
