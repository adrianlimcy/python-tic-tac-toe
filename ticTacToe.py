#this code is written as scripts
#game_board = ['_']*9 #this will create 9 underscores
#print (game_board[0]+'|'+game_board[1]+'|'+game_board[2])
#print (game_board[3]+'|'+game_board[4]+'|'+game_board[5])
#print (game_board[6]+'|'+game_board[7]+'|'+game_board[8])

#code from models

#code for user input
#while True:
#	pos = input("Enter any postion you want from (0-8): \n")
#	pos =int(pos)
#	game_board[pos]='X'
#	print (game_board[0]+'|'+game_board[1]+'|'+game_board[2])
#	print (game_board[3]+'|'+game_board[4]+'|'+game_board[5])
#	print (game_board[6]+'|'+game_board[7]+'|'+game_board[8])

won = False #at first we don't have any winners

choices = []
for pos in range(0,9):
	choices.append(str(pos+1))

#creating the Boolean variable
Is_Current_One = True #default player is player X

#first move is done by player X
while not won:
#board layout
	print ('\n')
	print ('|'+choices[0]+'|'+choices[1]+'|'+choices[2]+'|')
	print ('_________')
	print ('|'+choices[3]+'|'+choices[4]+'|'+choices[5]+'|')
	print ('_________')
	print ('|'+choices[6]+'|'+choices[7]+'|'+choices[8]+'|')
	
	if Is_Current_One:
		print("Player X")
	else:
		print("Player O")
		
	try:
		choice = int(input("> ").strip())
	except:
		print("Please enter only valid fields from the board (0-8)")
#		continue
	if Is_Current_One:
		choices[choice-1]="X"
	else:
		choices[choice-1]="O"
	Is_Current_One = not Is_Current_One

	#logic to make any player winner
	for pos_x in range(0,3):
		pos_y = pos_x * 3

		#for row condition:
		if (choices[pos_y] == choices[(pos_y + 1)]) and (choices[pos_y] == choices[(pos_y + 2)]):
			#code to change won to True
			won = True #main loop will break
		#column condition:
		if (choices[pos_x]==choices[(pos_x+3)]) and (choices[pos_x]==choices[(pos_x+6)]):
			won = True #main loop will break

		#for diagonal conditions:
		if ((choices[0] == choices[4] and choices[0]==choices[8]) or (choices[2] == choices[4] and choices[2]==choices[6])):
			won = True
	
#print who is winner
print("Player "+ str(int(Is_Current_One + 1)) + " won, Congratulations!")
		