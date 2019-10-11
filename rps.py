
import random 

COMPUTER_WINS = 1
PLAYER_WINS = 2
TIE = 0
INVALID = 3
ROCK = 1
PAPER = 2
SCISSORS = 3qq
tie_flag = True
def main():
	tie_flag = True
	while tie_flag == True: 
		computer = random.randint(1,3)
		player = int(input('Enter 1 for rock, 2 for paper, 3 for scissors:'))
		print('playerchose:', choiceString(player))
		print('computerchose:', choiceString(computer))
		if choiceString(player) != 'Something went wrong': 
			rps = rockPaperScissors(player, computer)
			if rps == PLAYER_WINS:
				print('player won!')
				tie_flag = False
			elif rps == COMPUTER_WINS:
				print('computer won!')
				tie_flag = False
			elif rps == TIE:
				print('congrats its a TIE!')
		else: 
			print('You made an invalid choice. No winner')
def rockPaperScissors(player,computer):
	if player == 1: 
		if computer == 2:
			return COMPUTER_WINS
		elif computer == 3:
			return PLAYER_WINS
		elif computer == 1:
			return TIE
	elif player == 2: 
		if computer == 2:
			return TIE
		elif computer == 3:
			return COMPUTER_WINS 
		elif computer == 1:
			return PLAYER_WINS
	elif player == 3: 
		if computer == 2:
			return PLAYER_WINS
		elif computer == 3:
			return TIE
		elif computer == 1:
			return COMPUTER_WINS
def choiceString(choice):
	if choice == 1:
		return 'rock'
	elif choice == 2: 
		return 'paper'
	elif choice == 3:
		return 'scissors'
	else:  
		return 'Something went wrong'
main()



