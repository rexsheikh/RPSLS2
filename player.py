from gesture import Gesture
from gestures import Gestures

class Player ():
    def __init__(self):
        self.score = 0
        self.rock = Gesture('rock',['paper','spock'])
        self.paper = Gesture('paper',['scissors','lizard'])
        self.scissor = Gesture('scissors',['rock','scissors'])
        self.lizard = Gesture('lizard',['rock','scissors'])
        self.spock = Gesture('spock', ['paper','lizard'])
        self.gestures = (self.rock,self.paper,self.scissor,self.lizard,self.spock)
        self.gestures_obj = Gestures()
        self.gestures_obj.gestures_list.extend(self.gestures)
        self.gestures_list = self.gestures_obj.gestures_list

    def increment_score(self):
        self.score += 1

    def choose_gesture(self):
        pass
    
    
