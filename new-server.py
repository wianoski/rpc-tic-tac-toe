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

def main():
    # Create server
    server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler, logRequests=True)
    server.register_introspection_functions()
    server.register_function(new_game, 'new_game')
    
    try:
        print "Server is running... You can start playing tic-tac-toe! (Use Control-C to exit)"
        server.serve_forever()
    except KeyboardInterrupt:
        print '...Exiting...'
        quit()

if __name__ == "__main__":
	main()
