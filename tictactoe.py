#Tic Tac Toe game
one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9

player1_mark = 'X'
player2_mark = 'O'

def check_winner(player_no):
	if one == player_no and two == player_no and three == player_no:
		return True
	elif four == player_no and five == player_no and six == player_no:
		return True
	elif seven == player_no and eight == player_no and nine == player_no:
		return True
	elif one == player_no and four == player_no and seven == player_no:
		return True
	elif two == player_no and five == player_no and eight == player_no:
		return True
	elif three == player_no and six == player_no and nine == player_no:
		return True
	elif one == player_no and five == player_no and nine == player_no:
		return True
	elif three == player_no and five == player_no and seven == player_no:
		return True
	else : pass

def check_tie(lst):
	if len(set(lst)) == 2:
		print "Tie game ;)"
		return True
	else : pass

def print_gameboard():
	print '''
	Tic Tac Toe Game

	__{a}__|__{b}__|__{c}__
	__{d}__|__{e}__|__{f}__
	  {g}  |  {h}  |  {i}
	'''.format(a=one, b=two, c=three, d=four, e=five, f=six, g=seven, h=eight, i=nine)

while True:
	print_gameboard()

	if check_winner(player2_mark): 
		print "Player 2 wins!!!"
		break
	while True:
		try :
			player_1_choice = int(raw_input('Player 1 (X): Please mark a spot with the number of your choice: '))
		except : 
			print "------Not a valid selection. Please try again-----"
			continue

		if player_1_choice == 1 and one != player1_mark and one != player2_mark: one = player1_mark
		elif player_1_choice == 2 and two != player1_mark and two != player2_mark: two = player1_mark
		elif player_1_choice == 3 and three != player1_mark and three != player2_mark: three = player1_mark
		elif player_1_choice == 4 and four != player1_mark and four != player2_mark: four = player1_mark
		elif player_1_choice == 5 and five != player1_mark and five != player2_mark: five = player1_mark
		elif player_1_choice == 6 and six != player1_mark and six != player2_mark: six = player1_mark
		elif player_1_choice == 7 and seven != player1_mark and seven != player2_mark: seven = player1_mark
		elif player_1_choice == 8 and eight != player1_mark and eight != player2_mark: eight = player1_mark
		elif player_1_choice == 9 and nine != player1_mark and nine != player2_mark: nine = player1_mark
		else : 
			print "\n------Not a valid selection. Please try again-----"
			continue
		break

	print_gameboard()

	if check_winner(player1_mark): 
		print "Player 1 wins!!!"
		break
	#list to check for ties with set()
	numlst = [one, two, three, four, five, six, seven, eight, nine]
	if check_tie(numlst) : break
	while True:
		try :
			player_2_choice = int(raw_input('Player 2 (O): Please mark a spot with the number of your choice: '))
		except : 
			print "------Not a valid selection. Please try again-----"
			continue

		if player_2_choice == 1 and one != player1_mark and one != player2_mark: one = player2_mark
		elif player_2_choice == 2 and two != player1_mark and two != player2_mark: two = player2_mark
		elif player_2_choice == 3 and three != player1_mark and three != player2_mark: three = player2_mark
		elif player_2_choice == 4 and four != player1_mark and four != player2_mark: four = player2_mark
		elif player_2_choice == 5 and five != player1_mark and five != player2_mark: five = player2_mark
		elif player_2_choice == 6 and six != player1_mark and six != player2_mark: six = player2_mark
		elif player_2_choice == 7 and seven != player1_mark and seven != player2_mark: seven = player2_mark
		elif player_2_choice == 8 and eight != player1_mark and eight != player2_mark: eight = player2_mark
		elif player_2_choice == 9 and nine != player1_mark and nine != player2_mark: nine = player2_mark
		else : 
			print "\n------Not a valid selection. Please try again-----"
			continue
		break

print "Game Over"