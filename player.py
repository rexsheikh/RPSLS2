from gesture import Gesture
from gestures import Gestures

class Player ():
    def __init__(self):
        self.score = 1
        self.gestures = Gestures()

    def increment_score(self):
        self.score += 1

    def choose_gesture(self):
        pass
    
    
