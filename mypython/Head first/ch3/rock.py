import random

#winner変数を用意する
winner = ''

#乱数からコンピューターの手を生成する
random_choice = random.randint(0,2)
if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
        computer_choice = 'paper'
else:
            computer_choice = 'scissors'

#ユーザーの手を聞く
user_choice = ''
while (user_choice != 'rock' and
       user_choice != 'paper' and
       user_choice != 'scissors'):
    user_choice = input('rock paper or scissors? ')

#ゲームロジックで勝敗を決定
if computer_choice == user_choice:
    winner = 'Tie'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'

#出力する
if winner == 'Tie':
    print('We both chose', computer_choice + ', play again')
else:
    print('You chose', user_choice, 'and the computer chose', computer_choice, 'The', winner, 'wins!')
