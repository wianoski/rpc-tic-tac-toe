from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from random import randint

import random
import sys
import copy

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
	    rpc_paths = ('/tic-tac-toe',)

# Create Game Hub
games = {}

def new_game():
    game_id = randint(0, 9999999)

    # To be sure unique game_id accross games
    while game_id in games:
        game_id = randint(0, 9999999)

    # Creating initial board
    board = []
    for i in range(9):
        board.append(-1)
    games[game_id] = board
    print "New game is created: " + str(game_id)
    return game_id

def new_move(game_id, index):
    board = games[game_id]
    board[index] = 1
    # ai_move_index = _new_ai_move_index(copy.deepcopy(board))
    # if ai_move_index != None:
	# 	board[ai_move_index] = 0
    games[game_id] = board
    return board

# def _new_ai_move_index(board):

#     # check if bot can win in the next move
#     for i in range(0,len(board)):
#         board_copy = copy.deepcopy(board)
#         if _is_move_valid(board_copy, i):
# 			board_copy[i] = 0
# 			if _check_win(board_copy) == 0:
# 				return i

#     # check if player could win on his next move
#     for i in range(0,len(board)):
#         board_copy = copy.deepcopy(board)
#         if _is_move_valid(board_copy, i):
#             board_copy[i] = 1
#             if _check_win(board_copy) == 1:
# 				return i

#     # check for space in the corners, and take it
#     move = _choose_random_move(board, [0,2,6,8])
#     if move != None:
# 		return move

#     # If the middle is free, take it
#     if _is_move_valid(board,4):
# 		return 4


#     # else, take one free space on the sides
#     move = _choose_random_move(board, [1,3,5,7])
#     return move

# def _choose_random_move(board, move_list):
#     possible_winning_moves = []
#     for index in move_list:
#         if _is_move_valid(board, index):
#             possible_winning_moves.append(index)

#     if len(possible_winning_moves) != 0:
#         return random.choice(possible_winning_moves)
#     else:
#         return None

def is_move_invalid(game_id, index1, index2):
    board = games[game_id]
    return board[index] != -1

def _is_move_valid(board, index):
	return board[index] == -1

def check_win(game_id):
    board = games[game_id]
    return _check_win(board)

def _check_win(board):
        
        #     1   | 2   | 3   | 4   | 5   |
        # ----------------------------------
        #     6   | 7   | 8   | 9   | 10   |
        # ----------------------------------
        #     11   | 12   | 13   | 14   | 15   |
        # ----------------------------------
        #     16   | 17   | 18   | 19   | 20   |
        # ----------------------------------
        #     21   | 22   | 23   | 24   | 25   |
        # ----------------------------------
        
    # win_cond = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
    win_cond = ((1,2,3),(2,3,4),(3,4,5),
                (6,7,8),(7,8,9),(8,9,10),
                (11,12,13),(12,13,14),(13,14,15),
                (16,17,18),(17,18,19),(18,19,20),
                (21,22,23),(22,23,24),(23,24,25),
                (1,6,11),(6,11,16),(11,16,21),
                (2,7,12),(7,12,17),(12,17,21),
                (3,8,13),(8,13,18),(13,18,23),
                (4,9,14),(9,14,19),(14,19,24),
                (5,10,15),(10,15,20),(15,20,25),
                (1,7,13),(2,8,14),(3,9,15),
                (6,2,18),(7,3,19),(8,14,20),
                (11,17,23),(12,18,24),(13,19,25),
                ) # baru kondisi di horizontal
    for each in win_cond:
        try:
            if board[each[0]-1] == board[each[1]-1] and board[each[1]-1] == board[each[2]-1]:
                return board[each[0]-1]
        except:
            pass
    return -1

def end_game(game_id):
    print "Game is ended " + str(game_id)
    del games[game_id]
    return True

def main():
    # Create server
    server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler, logRequests=True)
    server.register_introspection_functions()
    server.register_function(new_game, 'new_game')
    server.register_function(new_move, 'new_move')
    server.register_function(is_move_invalid, 'is_move_invalid')
    server.register_function(check_win, 'check_win')
    server.register_function(end_game, 'end_game')

    try:
        print "Server is running... You can start playing tic-tac-toe! (Use Control-C to exit)"
        server.serve_forever()
    except KeyboardInterrupt:
        print '...Exiting...'
        quit()

if __name__ == "__main__":
	main()
