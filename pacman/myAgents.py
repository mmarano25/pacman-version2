from pacman import Directions
from game import Agent
import api
import random
import game
import util
"""
class GoWestAgent(Agent):
	def getAction(self, state):
	    legal = api.legalActions(state)
        if( Directions.WEST in legal ):
            return api.makeMove(Directions.WEST,legal)
        else:
            if Directions.STOP in legal:
                legal.remove(Directions.STOP)
            return api.makeMove( random.choice(legal), legal)
"""

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
        last = Directions.STOP
        corners = []

    def getAction(self,state):
        legal = api.legalActions(state)
        corners = api.corners(state)
        print corners
        return api.makeMove( random.choice(api.legalActions(state)), legal)

