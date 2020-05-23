
from pprint import pprint

board = [
	[6, 0,  0,  0,  0,  3,  0,  0,  1],
	[0,  9,  0,  0,  0,  0,  0,  0,  3],
	[4,  0,  3,  0,  0,  0,  6,  0,  0,],
	[0,  0,  0,  5,  9,  0,  2,  0,  6],
	[0,  0,  0,  0,  0,  0,  0,  0,  0,],
	[0,  0,  7,  0,  0,  0,  0,  0,  4],
	[0,  0,  0,  0,  0,  0,  1,  7,  0,],
	[0,  0,  2,  0,  0,  8,  0,  0,  0,],
	[0,  0,  8,  0,  0,  0,  0,  4,  2]

]


# board = [
# 	[7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
#     [0,4,9,2,0,6,0,0,7]
# ]

def print_board(board):
	print("")
	for i in range(len(board)):
		if i%3 == 0 and i != 0:
			print('- - - - - - - - - - - ')
		for j in range(len(board[i])):
			if j% 3 == 0 and j != 0:
				print('| ' + str(board[i][j]) + ' ', end="")
			elif j == len(board[i]) - 1:
				print(board[i][j])
			
			else:
				print(str(board[i][j]) + ' ', end="")
	print("")

def find_empty(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				return (i,j)
	return None

def valid(board, num, pos):
	for i in range(len(board[0])):
		if board[pos[0]][i] == num and pos[1] != i:
			return False

	for i in range(len(board)):
		if board[i][pos[1]] == num and pos[0] != i:
			return False

	row_x = pos[1] // 3	
	row_y = pos[0] // 3	

	for i in range(row_y*3, row_y*3+3):
		for j in range(row_x*3, row_x*3+3):
			if board[i][j] == num and (i,j) != pos:
				return False

	return True

def solve(board):
	pos = find_empty(board)
	print(f'Empty Position: {pos}')
	if not pos:
		return True

	for i in range(1, len(board)+1):
		if valid(board, i, pos):
			board[pos[0]][pos[1]] = i
			print(f'trying value {i} at position {pos}')
			if solve(board):
				return True
			else:
				print(f'value failed {i} at position {pos}, trying another value')
				board[pos[0]][pos[1]] = 0

	return False

print_board(board)
solve(board)
print_board(board)
