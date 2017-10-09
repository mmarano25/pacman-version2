from pacman import Directions
from game import Agent
import api
import random
import game
import util

class GoWestAgent(Agent):
    def getAction(self, state):
        legal = api.legalActions(state)
        if Directions.WEST in legal:
            return api.makeMove(Directions.WEST, legal)
        else:
            if Directions.STOP in legal:
                legal.remove(Directions.STOP)
            return api.makeMove(random.choice(legal), legal)

class CornerSeekingAgent(Agent):
    def __init__(self):
        self.last = Directions.STOP
        self.cornersToSeek = list()
        self.first_call = True
        self.current_corner = ''

    def getAction(self,state):
        if first_call:
            for corner in api.corners(state):
                self.cornersToSeek.append(corner)
            self.first_call = False

        legal = api.legalActions(state)
        my_coord = api.whereAmI(state)
        
        

        return api.makeMove( random.choice(api.legalActions(state)), legal)


# figure out how to get to a corner.
#   see which direction corner is in: max(corner - my_coord)
# for corners: 2 3
#              0 1
# 
# 0: S E
# 1: S W
# 2: N E
# 3: N W

# note: only take action when last move is not legal.
#     will that affect avoiding ghosts?
